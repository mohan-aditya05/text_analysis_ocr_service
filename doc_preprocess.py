from db import MongoDB
from common import convert_pdf_to_images, generate_hash
from ocr import *
from google_ocr import GoogleOCR

class DocumentPreprocess:
    def __init__(self, file_bytes):
        self.file_bytes = file_bytes
        self.mongo = MongoDB()
        self.ocr = GoogleOCR()
    
    def process_document(self):
        hash_id = generate_hash(self.file_bytes)
        result = self.mongo.query_document({"hash_id":hash_id})
        if result:
            pdf_text = result['text']
        else:
            images = convert_pdf_to_images(self.file_bytes)
            pdf_text = self.ocr.get_text_response(images)
        
            ipt = {
                "hash_id": hash_id,
                "text": pdf_text
            }
            self.mongo.insert_document(ipt)
        
        return pdf_text
    

if __name__=="__main__":
    f_bytes = open("file.pdf", "rb")

    d = DocumentPreprocess(f_bytes)
    print(d.process_document())
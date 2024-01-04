# Copyright 2023 Aditya Mohan

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from db import MongoDB
from google_ocr import GoogleOCR
from common import convert_pdf_to_images, generate_hash, img_bytes_to_pil

class DocumentPreprocess:
    def __init__(self, file_bytes):
        self.file_bytes = file_bytes
        self.mongo = MongoDB()
        self.ocr = GoogleOCR()
    
    def process_document(self) -> str:
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
    
    def process_image(self) -> str:
        hash_id = generate_hash(self.file_bytes)
        result = self.mongo.query_document({"hash_id":hash_id})
        if result:
            img_text = result['text']
        else:
            images = [img_bytes_to_pil(self.file_bytes)]
            img_text = self.ocr.get_text_response(images)
        
            ipt = {
                "hash_id": hash_id,
                "text": img_text
            }
            self.mongo.insert_document(ipt)
        
        return img_text
    

if __name__=="__main__":
    f_bytes = open("file.pdf", "rb")

    d = DocumentPreprocess(f_bytes)
    print(d.process_document())
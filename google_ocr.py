import pytesseract
from ocr import OCR

class GoogleOCR:
    def get_text_response(self, images: list):
        pdf_texts = []
        for image in images:
            text = pytesseract.image_to_string(image)
            pdf_texts.append(text)
        return pdf_texts
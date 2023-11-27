import pytesseract
from ocr import OCR


class GoogleOCR(OCR):
    def get_text_response(self, images: list) -> list:
        """Generates ocr response from list of images

        Args:
            images (list): _description_

        Returns:
            list: _description_
        """
        pdf_texts = []
        for image in images:
            text = pytesseract.image_to_string(image)
            pdf_texts.append(text)
        return pdf_texts


# class AWS(OCR):
#     def get_text_response(self, images: list):
#         return super().get_text_response(images)

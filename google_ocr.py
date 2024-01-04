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

import pytesseract
from ocr import OCR


class GoogleOCR(OCR):
    def get_text_response(self, images: list) -> list:
        """Generates ocr response from list of images

        Args:
            images (list): list of images

        Returns:
            list: list of texts for each image
        """
        pdf_texts = []
        for image in images:
            text = pytesseract.image_to_string(image)
            pdf_texts.append(text)
        return pdf_texts


# class AWS(OCR):
#     def get_text_response(self, images: list):
#         return super().get_text_response(images)

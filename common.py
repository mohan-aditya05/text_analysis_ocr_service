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

import io
import fitz
import hashlib
from PIL import Image


def convert_pdf_to_images(file_bytes):
    doc = fitz.Document(stream=file_bytes)
    zoom = 3
    images = []
    for page in doc:
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=map)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)

    return images


def img_bytes_to_pil(img_bytes: bytes) -> Image:
    """Constructs PIL Image object from passed image bytes

    Args:
        img_bytes (bytes): passed image bytes

    Returns:
        Image: PIL Image object
    """
    img_obj = Image.open(io.BytesIO(img_bytes))
    # img_obj_new = Image.frombytes("RGB", [img_obj.width, img_obj.height], img_bytes)
    return img_obj


def generate_hash(file_bytes: bytes) -> str:
    """Generates hash from bytes

    Args:
        file_bytes (bytes): _description_

    Returns:
        str: _description_
    """
    return hashlib.sha256(file_bytes).hexdigest()


if __name__ == "__main__":
    f_bytes = open("file.pdf", "rb").read()

    print(len(convert_pdf_to_images(f_bytes)))

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

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

def generate_hash(file_bytes):
    return hashlib.sha256(file_bytes).hexdigest()

if __name__=="__main__":
    f_bytes = open("file.pdf", "rb").read()

    print(len(convert_pdf_to_images(f_bytes)))


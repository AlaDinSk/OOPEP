import os.path
import secrets
from flask import current_app
import pytesseract
from PIL import Image
import re



def save_picture(picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.config['SERVER_PATH'], picture_fn)
    output_size = (125, 125)
    i = Image.open(picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

def extract_text_from_image(image_path):
    """Извлекает текст из изображения с помощью pytesseract."""
    image = Image.open(image_path)
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config, lang='rus')
    return text

def extract_name(text):
    """Извлекает ФИО из текста."""
    fio_pattern = re.compile(r'([А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+)')
    fio_match = fio_pattern.search(text)
    return fio_match.group(0) if fio_match else None

def extract_conditional_name(text):
    conditional_name_pattern = re.compile(r'(\d{5})')
    conditional_name_match = conditional_name_pattern.search(text)
    if conditional_name_match and conditional_name_match.group():
        return conditional_name_match.group()
    return None

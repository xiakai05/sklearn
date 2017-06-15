# -*- encoding:utf-8 -*-
import os
import traceback
from PIL import Image
from pytesseract import *

def ocr(img):
    try:
        image=Image.open(img)
        rs=image_to_string(image,config="-psm 10")
    except Exception ,e:
        exstr = traceback.format_exc()
        print exstr
        return "none"
    return rs


for fn in os.listdir("/home/drjr/Desktop/clearyzm/"):
    f="/home/drjr/Desktop/clearyzm/"+fn
    rs=ocr(f)
    print fn +"     "+rs

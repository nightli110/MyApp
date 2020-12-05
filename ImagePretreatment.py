import cv2
import os
import sys
import base64
import numpy as np
from PIL import Image
import io

#base64code to opencv image format
def base64toimageCV(b64code):
    missing_padding = 4 - len(b64code) % 4
    if missing_padding:
        b64code += '='* missing_padding
    image_b64decode=base64.b64decode(b64code)
    img_array = np.fromstring(image_b64decode, np.uint8)
    img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)

    return img

#base64code to PIL
def base64toimagePIL(b64code):
    img_64decode = base64.b64decode(b64code)
    image = io.BytesIO(img_64decode)
    
    img = Image.open(image)
    return img


#OPENCV:imagetobase64
def imgetobase64(img):
    image = cv2.imencode('.jpg',img)[1]
    image_code = str(base64.b64encode(image))[2:-1]
    return image_code
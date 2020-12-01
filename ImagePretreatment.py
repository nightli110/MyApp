import cv2
import os
import sys
import base64
import numpy as np
from PIL import Image
import io

#base64code to opencv image format
def base64toimageCV(b64code):
    image_b64decode=base64.b64decode(b64code)
    img_array = np.fromstring(image_b64decode, np.uint8)
    img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)

    return img

#base64code to 
def base64toimagePIL(b64code):
    img_64decode = base64.b64decode(b64code)
    image = io.BytesIO(img_64decode)
    
    img = Image.open(image)
    return img

def drawrectangle(img,detections):
    confidence = detections[0, 0, i, 2]
    pass

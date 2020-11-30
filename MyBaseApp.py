import configparser
import multiprocessing
import http
from MessageQueue import *
import time
import cv2
import gc

class BaseApplication():
    def __init__(self):
        pass

    def loadmodel(self):
        pass

    def unloadmodel(self):
        pass
    
    def runmodel(self):
        pass


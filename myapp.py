import configparser
import multiprocessing
import http
from Messagequeue import *

class MyApplication(object):
    def __init__(self):
        self.hasmodel = multiprocessing.Manager().Value('i', 0)
        pass


    def loadmodel(self, path):
        
        pass

    def dumpmodel(self):
        pass

    def Isloadmodel(self):
        pass
    
    def runmodel(self, data):


import configparser
import multiprocessing
import http
from MessageQueue import *
import time
import cv2
import gc
##caffeexample
class MyApplication():
    def __init__(self):
        self.modellable=False
        self.lock=multiprocessing.RLock()
        self.net=cv2.dnn.readNetFromCaffe(prototxt, model)
        pass


    def loadmodel(self, prototxt, model):
        self.lock.acquire()
        self.net = cv2.dnn.readNetFromCaffe(prototxt, model)
        self.modellable=True
        self.lock.release()
        

    def uloadmodel(self):
        self.lock.acquire()
        del self.net
        gc.collect()
        self.modellable=False
        self.lock.release()
        

    def Isloadmodel(self):
        return self.modellable
        
    
    def runmodel(self, data=None):
        self.lock.acquire()
        if not self.Isloadmodel():
            self.lock.release()
            print("nomodel load plase load model first")
        self.net.setInput(data)
        netoutput=self.net.forward()
        self.lock.release()
        return netoutput

        

application=MyApplication()

def procedata():
    while(True):
        proceuuid=APPMessagelist.msgqueue.get()
        message=APPMessagelist.msgdict[proceuuid]
        application.runmodel()
        outputsuccess=APPMessagelist.prodmsgadd(message)
        time.sleep(0.1)
        APPqueuedict.senddata(proceuuid, message)
      

        


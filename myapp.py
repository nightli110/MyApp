import configparser
import multiprocessing
import http
from Messagequeue import *
import time
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
    
    def runmodel(self, data=None):
        print('runmodel')
        pass

application=MyApplication()

def procedata():
    while(True):
        proceuuid=APPMessagelist.msgqueue.get()
        message=APPMessagelist.msgdict[proceuuid]
        application.runmodel()
        p=1
        outputsuccess=APPMessagelist.prodmsgadd(message)
        time.sleep(0.1)
        APPqueuedict.senddata(proceuuid, message)
      

        


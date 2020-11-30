import cv2
import gc
import multiprocessing

from MyBaseApp import*


##caffeexample
class MyApplication(BaseApplication):
    def __init__(self):
        self.modellable=multiprocessing.Value('b', 0)
        self.lock=multiprocessing.RLock()
        self.loadlabel=multiprocessing.Queue()
        
        pass


    def loadmodel(self, prototxt, model):
        self.lock.acquire()
        if self.modellable.value==0:
            self.net = cv2.dnn.readNetFromCaffe(prototxt, model)
            self.modellable.value=1
            self.loadlabel.set(True)
        else:
            print("model has be load, unload first")
        self.lock.release()
        

    def gcmodel(self):
        self.lock.acquire()
        del self.net
        gc.collect()
        self.modellable.value=0
        self.lock.release()
    
    def unloadmodel(self):
        self.lock.acquire()
        self.modellable.value=0
        self.lock.release()
        

    def Isloadmodel(self):
        if self.modellable.value==0:
            return False
        else:
            return True

        
    
    def inferdata(self, data=None):
        self.lock.acquire()
        if not self.Isloadmodel():
            self.lock.release()
            print("nomodel load plase load model first")
        self.net.setInput(data)
        netoutput=self.net.forward()
        self.lock.release()
        return netoutput
        
    def advanceproc(self, frame):
        frame_resized=cv2.resize(frame,(300,300))
        blob = cv2.dnn.blobFromImage(frame_resized, 0.007843, (300, 300), (127.5, 127.5, 127.5), False)
        return blob

    def runnet(self):
        while(True):
            loadmodellabel=self.loadlabel.get()
            if loadmodellabel==True:
                while(True):
                    proceuuid=APPMessagelist.msgqueue.get()
                    message=APPMessagelist.msgdict[proceuuid]
                    netinput=self.advanceproc(message['img'])
                    netoutput=self.inferdata(message)
                    outputsuccess=APPMessagelist.prodmsgadd(message)
                    APPqueuedict.senddata(proceuuid, message)
                    if (self.modellable.value==0):
                        self.gcmodel()
                        break
    

application=MyApplication()

def modelinnet():
    if (application.Isloadmodel()==0):
        return False
    else:
        return True
    


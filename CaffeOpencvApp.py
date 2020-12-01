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
        self.manager=multiprocessing.Manager().dict()
        
        pass


    def loadmodel(self, netframe,modelfile):
        loadsuccess=True
        self.lock.acquire()
        if self.modellable.value==0:
            if netframe=="caffe":
                # net = cv2.dnn.readNetFromCaffe(modelfile[0], modelfile[1])
                # self.manager['net']=net
                self.modellable.value=1
                self.loadlabel.put(modelfile)
                time.sleep(1)
        else:
            print("model has be load, unload first")
            loadsuccess=False
        self.lock.release()
        return loadsuccess
        

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
        netoutput=None
        if not self.Isloadmodel():
            print("nomodel load plase load model first")
        else:
            self.net.setInput(data)
            netoutput=self.net.forward()
        # self.net.setInput(data)
        # netoutput=self.net.forward()
        self.lock.release()
        return netoutput
        
    def advanceproc(self, frame):
        frame_resized=cv2.resize(frame,(300,300))
        blob = cv2.dnn.blobFromImage(frame_resized, 0.007843, (300, 300), (127.5, 127.5, 127.5), False)
        return blob

    def runnet(self):
        while(True):
            time.sleep(1)
            modelfile=self.loadlabel.get()
            modelfile=('modelweight/MobileNetSSD_deploy.prototxt', 'modelweight/MobileNetSSD_deploy.caffemodel')
            self.net=cv2.dnn.readNetFromCaffe(modelfile[0], modelfile[1])
            print(modelfile)
            if self.modellable.value==1:
            # if True:
                while(True):
                    time.sleep(1)
                    proceuuid=APPMessagelist.msgqueue.get()
                    message=APPMessagelist.msgdict[proceuuid]
                    netinput=self.advanceproc(message['img'])
                    netoutput=self.inferdata(netinput)
                    outputsuccess=APPMessagelist.prodmsgadd(message)
                    APPqueuedict.senddata(proceuuid, message)
                    # if (self.modellable.value==0):
                    #     self.gcmodel()
                    #     break
    

application=MyApplication()

def modelinnet():
    if (application.Isloadmodel()==0):
        return False
    else:
        return True
    


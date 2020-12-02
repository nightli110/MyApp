import cv2
import gc
import multiprocessing
from MyConf import*

from MyBaseApp import*


##caffeexample
classNames = { 0: 'background',
    1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
    5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
    10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse',
    14: 'motorbike', 15: 'person', 16: 'pottedplant',
    17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor' }

class MyApplication(BaseApplication):
    def __init__(self):
        self.modellable=multiprocessing.Value('b', 0)
        self.lock=multiprocessing.RLock()
        self.loadlabel=multiprocessing.Queue()
        self.manager=multiprocessing.Manager().dict()
        
        pass

    ##获取全局配置
    def setglobalconf(self,conf):
        self.globalconf=conf

    #加载模型
    def loadmodel(self, netframe,modelfile):
        loadsuccess=True
        self.lock.acquire()
        if self.modellable.value==0:
            if netframe=="caffe":
                self.modellable.value=1
                self.loadlabel.put(modelfile)
                time.sleep(1)
        else:
            print("model has be load, unload first")
            loadsuccess=False
        self.lock.release()
        return loadsuccess
        
    ##判读模型是否在内存中
    def Isloadmodel(self):
        if self.modellable.value==0:
            return False
        else:
            return True

    ##卸载模型
    def unloadmodel(self):
        self.lock.acquire()
        self.modellable.value=0
        self.lock.release()

    #回收模型内存
    def gcmodel(self):
        self.lock.acquire()
        del self.net
        gc.collect()
        self.modellable.value=0
        self.lock.release()
    
    ##对消息内数据进行预处理，对于opencv dnn为转换成blob类型
    def advanceproc(self, frame):
        frame_resized=cv2.resize(frame,(300,300))
        blob = cv2.dnn.blobFromImage(frame_resized, 0.007843, (300, 300), (127.5, 127.5, 127.5), False)
        return blob

    ##对数据进行推理
    def inferdata(self, data=None):
        self.lock.acquire()
        netoutput=None
        if not self.Isloadmodel():
            print("nomodel load plase load model first")
        else:
            self.net.setInput(data)
            netoutput=self.net.forward()
        self.lock.release()
        return netoutput
        

    #推理进程函数
    def runnet(self):
        while(True):
            time.sleep(1)
            modelfile=self.loadlabel.get()
            modelfile=('modelweight/MobileNetSSD_deploy.prototxt', 'modelweight/MobileNetSSD_deploy.caffemodel')
            self.net=cv2.dnn.readNetFromCaffe(modelfile[0], modelfile[1])
            print(modelfile)
            if self.modellable.value==1:
                while(True):
                    time.sleep(1)
                    proceuuid=APPMessagelist.msgqueue.get()
                    message=APPMessagelist.msgdict[proceuuid]
                    netinput=self.advanceproc(message['img'])
                    netoutput=self.inferdata(netinput)

                    outputsuccess=APPMessagelist.prodmsgadd(netoutput)
                    APPqueuedict.senddata(proceuuid, message)
                    if (self.modellable.value==0):
                        self.gcmodel()
                        break
    
    ##对推理结果进行处理
    def resultsproc(self,data,img):
        message={}
        lablelist=[]
        for i in range(data.shape[2]):
            confidence = data[0,0,i,2]
            if confidence>0.2:
                class_id = int(data[0,0,i,1])

                rows=self.globalconf.getoption('image_1', 'rows')
                cols=self.globalconf.getoption('image-1','cols')
                if rows==None or cols==None:
                    return None
                xLeftBottom = int(data[0,0,i,3]*cols)
                yLeftBottom = int(data[0, 0, i, 4]*rows)
                xRightTop = int(data[0,0,i,5]*cols)
                yRightTop = int(data[0,0, i, 6]*rows)

                widthFactor = img.shape[0]/cols
                heightFactor = img.shape[1]/rows

                xLeftBottom_ = int(widthFactor*xLeftBottom)
                yLeftBottom_ = int(heightFactor*yLeftBottom)
                xRightTop_ = int(widthFactor*xRightTop)
                yRightTop_ = int(heightFactor*yRightTop)

                cv2.rectangle(img,(xLeftBottom_, yLeftBottom_),(xRightTop_, yRightTop_))

                if class_id in classNames:
                    label = classNames[class_id]+"： "+str(confidence)
                    lablelist.append((label, [xLeftBottom_, yLeftBottom_, xRightTop_, yRightTop_]))

                    labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_TRIPLEX, 0.8, 1)

                    cv2.rectangle(img, (xLeftBottom_, yLeftBottom_ - labelSize[1]),
                                 (xLeftBottom_ + labelSize[0], yLeftBottom_ + baseLine),
                                 (255, 255, 255), cv2.FILLED)
                    cv2.putText(img, label, (xLeftBottom_, yLeftBottom_),
                        cv2.FONT_HERSHEY_TRIPLEX, 0.8, (0, 0, 0))
        message['image_1']=img
        message['text_1']=lablelist
        return message


application=MyApplication()

    


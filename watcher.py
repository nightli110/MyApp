import os
import psutil
import datetime
import time
from multiprocessing import Process
import multiprocessing


class Watcher(object):
    def __init__(self, pid):   
        self.__watchermsg = multiprocessing.Manager().dict()
        self.__WatchPid = pid
        self.__watchermsg['MaxRam'] = 0
        self.__watchermsg['Stop'] = False
        self.__watchermsg['Begintime']=0
        self.__watchermsg['Endtime']=0
        self.__watchermsg['infertime']=0
        self.__Lock=multiprocessing.RLock()

        

        self.__WatchPeocess = multiprocessing.Process(name="Watcher",target=self.WatchRam, args=())

    def WatchRam(self):
        while(1):
            self.__Lock.acquire()
            tempram=psutil.Process(self.__WatchPid).memory_info().rss/1024/1024/1024

            if(tempram>self.__watchermsg['MaxRam']):
               self.__watchermsg['MaxRam']=tempram
            time.sleep(0.01)
            self.__Lock.release()

    def StartRecod(self):
        self.__watchermsg['Begintime'] = datetime.datetime.now()

    def StopRecod(self):
        self.__watchermsg['Endtime'] = datetime.datetime.now()
        self.__watchermsg['infertime'] = self.__watchermsg['Endtime']-self.__watchermsg['Begintime']
    
    def GetInferTime(self):
        if self.__watchermsg['infertime']==0:
            print("there no time record")
        return self.__watchermsg['infertime']
    
    def GetMaxRam(self):
        if self.__watchermsg['MaxRam']==0:
            print("there no ram record")
        return self.__watchermsg['MaxRam']
    
    def Stop(self):
        self.__Lock.acquire()
        self.__WatchPeocess.terminate()
        self.StopRecod()
        self.__Lock.release()
    
    def Start(self):
        self.StartRecod()
        self.__WatchPeocess.start()
    
    def GetWatcherMsg(self):
        return self.__watchermsg

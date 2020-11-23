import os
import psutil
import datetime
import time
from multiprocessing import Process

class Watcher(object):
    def __init__(self, pid):
        self.__WatchPid = pid
        self.__MaxRam = 0
        self.__Stop=False
        self.__Begintime=0
        self.__Endtime=0
        self.__infertime=0

        self.__WatchPeocess = Process(name="Watcher",target=self.WatchRam, args=())

    def WatchRam(self):
        while(1):
            tempram=psutil.Process(self.__WatchPid).memory_info().rss/1024/1024/1024
            print (tempram)
            print(self.__WatchPid)
            if(tempram>self.__MaxRam):
               self.__MaxRam=tempram
            time.sleep(0.01)

    def BeginRecod(self):
        self.__Begintime = datetime.datetime.now()

    def StopRecod(self):
        self.__Endtime = datetime.datetime.now()
        self.__infertime = self.__Endtime-self.__Begintime
    
    def GetInferTime(self):
        if self.__infertime==0:
            print("there no time record")
        return self.__infertime
    
    def GetMaxRam(self):
        if self.__MaxRam==0:
            print("there no ram record")
        return self.__MaxRam
    
    def Stop(self):
        self.__WatchPeocess.terminate()
    
    def Start(self):
        self.__WatchPeocess.start()

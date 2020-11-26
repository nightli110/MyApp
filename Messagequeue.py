import multiprocessing
import json
import os


class Messagelist(object):
    def __init__(self, maxlen=100):
        self.msglist=multiprocessing.Manager().list()
        self.msgqueue=multiprocessing.Queue()
        self.lock = multiprocessing.RLock()
        self.queuemax = maxlen

    def add(self, message):
        self.lock.acquire()
        addsuccess=True
        msglen=len(self.msglist)
        if(msglen==self.queuemax):
            addsuccess=False
        else:
            self.msgqueue.put(message[uuid])
            self.msglist.append(message)
        self.lock.release()
        return addsuccess

    def pop(self):
        self.lock.acquire()
        if len(self.msglist)==0:
            topmessage=None
        else:
            topmessage=self.msglist[0]
            self.msglist.pop()
        self.lock.release()
        return topmessage

    def len(self):
        self.lock.acquire()
        queuelen=len(self.msglist)
        self.lock.release()
        return queuelen

    def setqueuelen(self, queuelen):
        self.lock.acquire()
        setsuccess= True
        nowlen= len(self.msglist)
        if nowlen>queuelen:
            setsuccess=False
        else:
            self.queuemax=queuelen
        self.lock.release()
        return setsuccess
    
    def getfront(self):
        self.lock.acquire()
        if len(self.msglist)==0:
            topmessage=None
        else:
            topmessage=self.msglist[0]
           
        self.lock.release()
        return topmessage

class Messagequeuedic(object):
    def __init__(self, maxlen=100):
        self.queuedict=multiprocessing.Manager().dict()
        self.lock = multiprocessing.RLock()
        self.queuedictlenmax = maxlen
    
    def setmaxlen(self,maxlen):
        self.lock.acquire()
        setsuccess = True
        if(len(self.queuedict)>=maxlen):
            setsuccess=False
        else:
            self.queuedictlenmax = maxlen
        self.lock.release()
        return setsuccess
    
    def addqueue(self, uuid):
        self.lock.acquire()
        addsuccess=True
        if (len(self.queuedict)==self.queuedictlenmax):
            addsuccess = False
        else:
            self.queuedict[uuid]=multiprocessing.Queue()
        self.lock.release()
        return addsuccess
    
    def removequeue(self, uuid):
        self.lock.acquire()
        addsuccess=True
        if (uuid in self.queuedict.keys()):
            self.queuedict.popitem(uuid)
        else:
            addsuccess=False
        self.lock.release()
        return addsuccess
    
    def recvdata(self, uuid):
        if uuid not in self.queuedict.keys():
            return None
        returndata= self.queuedict[uuid].get()
        return returndata
    

APPMessagelist = Messagelist()
APPqueuedict=Messagequeuedic()
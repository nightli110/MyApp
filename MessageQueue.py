import multiprocessing
import json
import os


class Messagelist(object):
    def __init__(self, maxlen=100):
        self.msgdict=multiprocessing.Manager().dict()
        self.prodmsg=multiprocessing.Manager().dict()
        self.msgqueue=multiprocessing.Queue()
        self.lock = multiprocessing.RLock()
        self.finishlock= multiprocessing.RLock()
        self.queuemax = maxlen

    def addmsg(self, message):
        self.lock.acquire()
        addsuccess=True
        msglen=len(self.msgdict)
        if(msglen==self.queuemax):
            addsuccess=False
        else:
            self.msgdict[message['uuid']]= message
            self.msgqueue.put(message["uuid"])
        self.lock.release()
        return addsuccess

    def removemsg(self, uuid):
        removesuccess= True
        self.lock.acquire()
        if uuid not in self.msgdict.keys():
            removesuccess=False
        else:
            self.msgdict.popitem(uuid)
        self.lock.release()
        return removesuccess

    def len(self):
        self.lock.acquire()
        queuelen=len(self.msgdict)
        self.lock.release()
        return queuelen

    def setqueuelen(self, queuelen):
        self.lock.acquire()
        setsuccess= True
        nowlen= len(self.msgdict)
        if nowlen>queuelen:
            setsuccess=False
        else:
            self.queuemax=queuelen
        self.lock.release()
        return setsuccess
    
    def getmsg(self,uuid):
        self.lock.acquire()
        topmessage=self.msgdict[uuid]
        self.lock.release()
        return topmessage
    
    def prodmsgadd(self,message):
        addsuccess =True
        self.finishlock.acquire()
        uuid=message['uuid']
        if uuid not in self.prodmsg.keys():
            self.prodmsg[uuid]=message
        else:
            addsuccess=False
        self.finishlock.release()
        return addsuccess

    def prodmsgremove(self, uuid):
        removesuccess= True
        self.finishlock.acquire()
        if uuid in self.prodmsg.keys():
            self.prodmsg.popitem(uuid)
        else:
            removesuccess=False
        self.finishlock.release()
        return removesuccess
    
    def prodmsgisexit(self, uuid):
        isexit=True
        self.finishlock.acquire()
        if uuid not in self.prodmsg.keys():
            isexit=False
        self.finishlock.release()
        return isexit


class Messagequeuedic(object):
    def __init__(self, maxlen=100):
        self.queuedict=multiprocessing.Manager().dict()
        self.manager = multiprocessing.Manager()
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
            self.queuedict[uuid]=self.manager.Queue()
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
    
    def senddata(self, uuid, message):
        sendsuccess= True

        if uuid not in self.queuedict.keys():
            sendsuccess=False
        else:
            self.queuedict[uuid].put(message)
        return sendsuccess
    

APPMessagelist = Messagelist()
APPqueuedict=Messagequeuedic()
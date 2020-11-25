import multiprocessing
import json
import os


class Messagequeue(object):
    def __init__(self, maxlen):
        self.msglist=multiprocessing.Manager().list()
        self.lock = multiprocessing.RLock()
        self.queuemax = maxlen

    def add(self, message):
        self.lock.acquire()
        addsuccess=True
        msglen=len(self.meglist)
        if(msglen==self.queuemax):
            addsuccess=False
        else:
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
        pass

    def 

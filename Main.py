import os
import psutil
import sys
import ServerConf
import MyConf
import MyServer
import multiprocessing
from CaffeOpencvApp import*

if __name__=='__main__':
    confpath='Conf.ini'
    Myconf = MyConf.Myconf(confpath)
    serverconf=ServerConf.watchserver(Myconf.isusegpu())
    
  
    if int(Myconf.usecenter()):
        pingresult=ServerConf.pingcenter(Myconf.getcenterip())
        if not pingresult:
            print('center not ready')
            exit()
        pass
    else:
        multiprocessing.Process(target=application.runmodel, args=()).start()
        MyServer.app.run()
        
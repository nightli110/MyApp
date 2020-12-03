import os
import psutil
import sys
import ServerConf
import MyConf
import MyServer
import multiprocessing
from CaffeOpencvApp import*
import logging
from MyLog import Mylog



if __name__=='__main__':
    configpath='./config/config.ini'
    Myconf = MyConf.Myconf(configpath)
    serverconf=ServerConf.watchserver(Myconf.isusegpu())
    MyServer.app.config['Myconf']=Myconf
    application.setglobalconf(Myconf)
    Mylog.initlog(Myconf)
    
  
    if int(Myconf.usecenter()):
        pingresult=ServerConf.pingcenter(Myconf.getcenterip())
        if not pingresult:
            print('center not ready')
            exit()
        pass
    else:
        multiprocessing.Process(target=application.runnet, args=()).start()
        MyServer.app.run()
        
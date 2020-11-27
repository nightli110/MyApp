import os
import psutil
import sys
import serverconf
import Myconf
import Myserver
import multiprocessing
import myapp

if __name__=='__main__':
    confpath='conf.ini'
    Myconf = Myconf.Myconf(confpath)
    serverconf=serverconf.watchserver(Myconf.isusegpu())
    
  
    if int(Myconf.usecenter()):
        pingresult=serverconf.pingcenter(Myconf.getcenterip())
        if not pingresult:
            print('center not ready')
            exit()
        pass
    else:
        multiprocessing.Process(target=myapp.procedata, args=()).start()
        Myserver.app.run()
        
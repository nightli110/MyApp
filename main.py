import os
import psutil
import sys
import serverconf
import Myconf

if __name__=='main':
    confpath='conf.ini'
    Myconf = Myconf.Myconf(confpath)
    serverconf=serverconf.watchserver(Myconf.isusegpu())

    if Myconf.usecenter():
        pingresult=serverconf.pingcenter(Myconf.getcenterip())
        if not pingresult:
            print('center not ready')
            exit()
        pass
    else:
        
     

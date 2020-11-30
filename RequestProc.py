import  json
import ServerConf
import os
import ErrorJson

def getnetframe(conf):
    netframe=conf.getoption('netcof', 'caffe')
    if (netframe=="caffe"):
        netweight=conf.getoption('netcof','weight')
        prototxt=conf.getoption('netcof','prototxt')
        if ()

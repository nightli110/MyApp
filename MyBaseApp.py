import configparser
import multiprocessing
import http
from MessageQueue import *
import time
import cv2
import gc

class BaseApplication():
    def __init__(self):
        pass

    #加载模型
    def loadmodel(self):
        pass

    ##判读模型是否在内存中
    def Isloadmodel(self):
        pass
    
    ##卸载模型
    def unloadmodel(self):
        pass
    
    #回收模型内存
    def gcmodel(self):
        pass
    
    #对消息数据进行预处理
    def advanceproc(self):
        pass
    
    #对推理结果进行处理
    def resultsproc(self):
        pass
    
    #对数据进行推理
    def inferdata(self, data=None):
        pass

    #推理进程
    def runmodel(self):
        pass

    

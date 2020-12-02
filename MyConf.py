import configparser
import os
import sys

class Myconf(object):
    def __init__(self, path):
        self.conf=configparser.ConfigParser()
        self.conf.read(path)
    
    def getsession(self,section):
        if self.conf.has_section(section):
            return self.conf.items(section)
        else:
            return None

    def getoption(self, section, option):
        
        if self.conf.has_option(section, option):
            return self.conf.get(section, option)
        else:
            return None
    
    def getcenterip(self):
        return self.conf.get('center','ip')

    def getcenterport(self):
        return self.conf.get('center', 'port')


    def getserverport(self):
        return self.conf.get('server', 'port')

    def usecenter(self):
        return self.conf.get('mode', 'use_center')


    def getapplicationinput(self):
        return self.conf.get('applcation','input')

    def isusegpu(self):
        return self.conf.get('application', 'usegpu')
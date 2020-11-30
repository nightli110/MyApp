#TODO 
#errorcode 
import json

#1****:服务相关的
#2****:消息队列相关的
#3****:模型相关的
#4****:配置相关的
#10001:inputerror
def inputerror(key):
    errormessage="the "+key+ " format is error"
    errdic={"10001":errormessage}
    errjson= json.dumps(errdic)
    return errjson


def messageadderror():
    errormessage= "the messagequeue add error"
    errdic={"20001":errormessage}
    errjson= json.dumps(errdic)
    return errjson

def queueadderror():
    errormessage= "the queue add error"
    errdic={"20002":errormessage}
    errjson= json.dumps(errdic)
    return errjson

def nomodelerror():
    errormessage= "no model in network"
    errdic={"30001":errormessage}
    errjson= json.dumps(errdic)
    return errjson

def nomodelerror():
    errormessage= "no model in network"
    errdic={"30001":errormessage}
    errjson= json.dumps(errdic)
    return errjson


def conferr(name):
    errormessage="conf file in section: "+name+" error"
    errdic={"40001":errormessage}
    errjson=json.dumps(errdic)
    return errjson

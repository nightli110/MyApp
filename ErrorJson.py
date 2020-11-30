#TODO 
#errorcode 
import json

#10001:inputerror
def inputerror(key):
    errormessage="the "+key+ " format is error"
    errdic={"10001":errormessage}
    errjson= json.loads(errdic)
    return errjson

def messageadderror():
    errormessage= "the messagequeue add error"
    errdic={"20001":errormessage}
    errjson= json.loads(errdic)
    return errjson

def queueadderror():
    errormessage= "the queue add error"
    errdic={"20002":errormessage}
    errjson= json.loads(errdic)
    return errjson



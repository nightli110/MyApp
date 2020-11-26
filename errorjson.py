#TODO 
#errorcode 
import json

#10001:inputerror
def inputerror(key):
    errormessage="the "+key+ " format is error"
    errdic={"10001":errormessage}
    errjson= json.loads(errdic)
    return errjson
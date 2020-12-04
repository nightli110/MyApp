
import json
import logging

#1****:服务相关的
#2****:消息队列相关的
#3****:模型相关的
#4****:配置相关的
#10001:inputerror

Errordic={
    10001:      "the %s format is error",
    20001:      "the messagequeue add error",
    20002:      "the queue add error",
    30001:      "no model in network",
    30002:      "model has in network， please unload first",
    40001:      "the config option %s format is error",
    40002:      "the %s option is empty"
}

logger=logging.getLogger('log02')
def jsonerrorcode(code, key=None):
    errmessage=None
    if key !=None:
        errmessage=Errordic[code].format(key)
    else:
        errmessage=Errordic[code]
    jsonerror={"code":code,
                "message":errmessage}
    jsonerror=json.dumps(jsonerror)
    logger.error(jsonerror)
    return jsonerror
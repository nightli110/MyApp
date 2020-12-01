import  json
import ServerConf
import os
import ErrorJson

def getnetframe(conf):
    netframe=conf.getoption('netconf', 'netframe')
    weightroot=conf.getoption('netconf', 'weightroot')
    if (netframe=="caffe"):
        netweight=os.path.join(weightroot,conf.getoption('netconf','weight'))
        prototxt=os.path.join(weightroot,conf.getoption('netconf','prototxt'))
        if netframe!=None and prototxt!=None:
            return (prototxt, netweight)
        else:
            return None
    elif (netframe=="pytorch"):
        pass
    elif (netframe=="tensorflow"):
        pass
    else:
        pass



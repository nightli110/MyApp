import json
import os
import ErrorJson

#example strinput:"image:2;text:2" 
#example input_name:["image_1","image_2","text_1", "text_2"]
#TODO检查输入是否合法
def getinputname(strinput):
    input_name={}
    strinput=strinput.split(';')
    for item in strinput:
        name_pair=item.split(':')
        if len(name_pair)!=2:
            print('the input is irregular')
            return None
        name_len= int(name_pair[1])
        for i in range(0, name_len):
            temp_name=name_pair[0]+'_'+str(i)
            input_name[temp_name]=name_pair[0]
    return input_name


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



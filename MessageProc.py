import json
import os
import ErrorJson
import base64
import ImagePretreatment

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
        for i in range(1, name_len+1):
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

###location:[(label,[xLeftBottom_, yLeftBottom_, xRightTop_, yRightTop_])......]
###outstring(string):label-[xLeftBottom_, yLeftBottom_, xRightTop_, yRightTop_];......
def labeltostring(textlist):
    outstring= ""
    for i in textlist:
        lable=i[0]
        location="["+str(i[1][0])+','+str(i[1][1])+','+str(i[1][2])+','+str(i[1][3])+']'
        outstring=outstring+lable+'-'+location+";"
    return outstring

def netoutputtomessage(netoutput):
    message={}
    for key in netoutput:
        key_type=key.split('_')[0]
        if key_type=='image':
            message[key]=ImagePretreatment.imgetobase64(netoutput[key])
            
        elif key_type=='text':
            outtext=labeltostring(netoutput[key])
            message[key]=outtext
        else:
            print("not support now")
    return json.loads(message)

def postdatatolog(data):
    returnstr=""
    if "uuid" in data.keys() and "input" in data.keys():
        returnstr="uuid: "+data["uuid"]+";"+"input: "+data["input"] +' '
    return returnstr
    

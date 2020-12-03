import os
import configparser
from MessageQueue import *
from flask import Flask, request, jsonify
from MessageProc import *
from ImagePretreatment import *
import time
import json
from ErrorJson import *
from CaffeOpencvApp import*

####
import cv2


app = Flask(__name__)
    
def Readconf(path):
    config = configparser.ConfigParser()
    config.read(path)
    port = config.get('server','port')
    return port

@app.route('/helloworld')
def hello_world():
    return 'Hello World!'


@app.route('/register')
def appregister():
    pass

#上下线
@app.route('/online', methods=["POST"])
def apponline():
    if request.method=="POST":
        data= json.loads(request.get_data())
        if data['loadmodel']==True:
            if not application.Isloadmodel():
                modelfile=getnetframe(app.config['Myconf'])
                loadsuccess=application.loadmodel(app.config['Myconf'].getoption('netconf', 'netframe'),modelfile)
                return "model online success"
            else:
                return jsonerrorcode(30002)
        elif data['loadmodel']==False:
            if not application.Isloadmodel():
                application.unloadmodel()
                return "model offline success"
            else:
                return jsonerrorcode(30001)
        else:
            return jsonerrorcode(10001, 'loadmodel')

#接受数据
@app.route('/postdata', methods=["POST"]) 
def postdata():
    if request.method=="POST":
        data=json.loads(request.get_data())
        inputnamelist=getinputname(data["input"])
        if inputnamelist==None:
            return inputerror("input")
        # for key in inputnamelist.keys():
        #     if inputnamelist[key]=="image"   :
        #         data[key]=base64toimageCV(inputnamelist[key])
        # if not modelinnet():
        #     return nomodelerror()
        uuid= data["uuid"]
        addsuccess=APPqueuedict.addqueue(uuid)
        img=cv2.imread('dog.jpg')
        data['img']=img
        if addsuccess==None:
            return jsonerrorcode(20002)
        addsuccess=APPMessagelist.addmsg(data)
        if addsuccess==None:
            return jsonerrorcode(20001)
        time.sleep(0.2)
        processdata=APPqueuedict.recvdata(uuid)
        return "ok"
        
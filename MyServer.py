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
import logging

####
import cv2


app = Flask(__name__)
@app.route('/helloworld')
def hello_world():
    logger.info('Hello World!')
    return 'Hello World!'


@app.route('/register')
def appregister():
    logger.info('TianDao is not completed, it int not allowed.')
    pass

#上下线
@app.route('/online', methods=["POST"])
def apponline():
    if request.method=="POST":
        data= json.loads(request.get_data())
        logger.info('get data message, the data keys: '+str(data.keys()))
        if data['loadmodel']==True:
            if not application.Isloadmodel():
                modelfile=getnetframe(app.config['Myconf'])
                loadsuccess=application.loadmodel(app.config['Myconf'].getoption('netconf', 'netframe'),modelfile)
                logger.info("model online success")
                return "model online success"
            else:
                return jsonerrorcode(30002)
        elif data['loadmodel']==False:
            if not application.Isloadmodel():
                application.unloadmodel()
                logger.info("model offline success")
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
        logdata=postdatatolog(data)
        if logdata==None: 
            return jsonerrorcode(10001, 'uuid and input')
        else:
            logger.info("get data: "+logdata)
        inputnamelist=getinputname(data["input"])
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
        
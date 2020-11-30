import os
import configparser
from MessageQueue import *
from flask import Flask, request, jsonify
from MessageProc import *
from ImagePretreatment import *
import time
import json
from ErrorJson import *

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

@app.route('/online')
def apponline():
    pass

@app.route('/postdata', methods=["POST"])
def postdata():
    if request.method=="POST":
        data=json.loads(request.get_data())
        inputnamelist=getinputname(data["input"])
        if inputnamelist==None:
            return inputerror("input")
        # for key in inputnamelist.keys():
        #     if inputnamelist[key]=="image":
        #         data[key]=base64toimageCV(inputnamelist[key])
        uuid= data["uuid"]
        addsuccess=APPqueuedict.addqueue(uuid)
        img=cv2.imread('dog.jpg')
        data['img']=img
        if addsuccess==None:
            return queueadderror()
        addsuccess=APPMessagelist.addmsg(data)
        if addsuccess==None:
            return messageadderror()
        time.sleep(0.2)
        processdata=APPqueuedict.recvdata(uuid)
        print('aaa')
        return "ok"
    return queueadderror()
        
    pass
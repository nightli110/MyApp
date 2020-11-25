import os
import configparser
from flask import Flask


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

@app.route('/postdata')
def postdata():
    pass
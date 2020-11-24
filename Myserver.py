import os
import configparser
from flask import Flask


port = 7000
app = Flask(__name__)
    
def Readconf(self,path):
    config = configparser.ConfigParser()
    config.read(path)
    port = config.get('server','port')
    return port

@app.route('/helloworld')
def hello_world(self):
    return 'Hello World!'


@app.route('/heart')
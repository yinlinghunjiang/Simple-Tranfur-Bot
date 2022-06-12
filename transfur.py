#coding=utf8 
import json
from flask import  Flask
from flask_bootstrap import Bootstrap
import datetime
import hashlib
import urllib3
import os
import traceback
from configparser import ConfigParser

app = Flask(__name__)
bootstrap = Bootstrap(app)
def sign(path,time):
    config = ConfigParser()
    config.read('./config/main.conf', encoding='UTF-8')
    key = config['Transfur']['key']
    #qq = config['Transfur']['qq']# 构造函数
    preSigned=path+"-"+str(time)+"-"+key
    return hashlib.md5(preSigned.encode(encoding='UTF-8')).hexdigest()
def qqfac():
    config = ConfigParser()
    config.read('./config/main.conf', encoding='UTF-8')
    #key = config['Transfur']['key']
    return config['Transfur']['qq']
@app.route('/')
def index():
    return 'Hello World!'
@app.route('/getFursuitByID/<furid>', methods=['GET'])
def getFursuitByID(furid):
    ts=datetime.datetime.now().timestamp()
    
    prsign=sign("api/v2/getFursuitByID",ts)
    http = urllib3.PoolManager()# 创建PoolManager对象生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
    resp=http.request('GET', 'https://api.tail.icu/api/v2/getFursuitByID?qq='+str(qqfac())+'&timestamp='+str(ts)+"&sign="+prsign+"&fid="+furid)
    print(resp.data.decode('UTF-8')) # get方式请求
    return str(resp.data.decode('UTF-8'))
@app.route('/getFursuitRand', methods=['GET'])
def getFursuitRand():
    ts=datetime.datetime.now().timestamp()
    
    prsign=sign("api/v2/getFursuitRand",ts)
    http = urllib3.PoolManager()  # 创建PoolManager对象生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
    resp=http.request('GET', 'https://api.tail.icu/api/v2/getFursuitRand?qq='+str(qqfac())+'&timestamp='+str(ts)+"&sign="+prsign)
    print(resp.data.decode('UTF-8')) # get方式请求
    return str(resp.data.decode('UTF-8'))
@app.route('/getFursuitByName/<name>', methods=['GET'])
def getFursuitByName(name):
    ts=datetime.datetime.now().timestamp()
    prsign=sign("api/v2/getFursuitByName",ts)
    http = urllib3.PoolManager()  # 创建PoolManager对象生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
    resp=http.request('GET', 'https://api.tail.icu/api/v2/getFursuitByName?qq='+str(qqfac())+'&timestamp='+str(ts)+"&sign="+prsign+"&name="+name)
    print(resp.data.decode('UTF-8')) # get方式请求
    return str(resp.data.decode('UTF-8'))
@app.route('/getimg/getFursuitByID/<fid>', methods=['GET'])
def getFursuitByIDimg(fid): # get方式请求
    data = json.loads(getFursuitByID(fid))
    return "<img src='"+data['data']['url']+"'>"
@app.route('/getimg/getFursuitRand', methods=['GET'])
def getFursuitRandimg(): # get方式请求
    data = json.loads(getFursuitRand())
    return "<img src='"+data['data']['url']+"'>"
@app.route('/getimg/getFursuitByName/<name>', methods=['GET'])
def getFursuitByNameimg(name): # get方式请求
    data = json.loads(getFursuitByName(name))
    return "<img src='"+data['data']['url']+"'>"
@app.route('/DailyFursuit/Rand/', methods=['GET'])
def DailyFursuitRand():
    ts=datetime.datetime.now().timestamp()
    prsign=sign("api/v2/DailyFursuit/Rand",ts)
    http = urllib3.PoolManager()  # 创建PoolManager对象生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
    resp=http.request('GET', 'https://api.tail.icu/api/v2/DailyFursuit/Rand?qq='+str(qqfac())+'&timestamp='+str(ts)+"&sign="+prsign)
    print(resp.data.decode('UTF-8')) # get方式请求
    return str(resp.data.decode('UTF-8'))
@app.route('/DailyFursuit/name/<name>', methods=['GET'])
def DailyFursuitByName(name):
    ts=datetime.datetime.now().timestamp()
    prsign=sign("api/v2/DailyFursuit/name",ts)
    http = urllib3.PoolManager()  # 创建PoolManager对象生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
    resp=http.request('GET', 'https://api.tail.icu/api/v2/DailyFursuit/name?qq='+str(qqfac())+'&timestamp='+str(ts)+"&sign="+prsign+"&name="+name)
    print(resp.data.decode('UTF-8')) # get方式请求
    return str(resp.data.decode('UTF-8'))
@app.route('/DailyFursuit/id/<furid>', methods=['GET'])
def DailyFursuitByID(furid):
    ts=datetime.datetime.now().timestamp()
    prsign=sign("api/v2/DailyFursuit/id",ts)
    http = urllib3.PoolManager()  # 创建PoolManager对象生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
    resp=http.request('GET', 'https://api.tail.icu/api/v2/DailyFursuit/id?qq='+str(qqfac())+'&timestamp='+str(ts)+"&sign="+prsign+"&id="+furid)
    print(resp.data.decode('UTF-8')) # get方式请求
    return str(resp.data.decode('UTF-8'))
@app.route('/getimg/DailyFursuit/Rand', methods=['GET'])
def getDailyFursuitRandimg(): # get方式请求
    data = json.loads(DailyFursuitRand())
    return "<img src='"+data['data']['url']+"'>"
@app.route('/getimg/DailyFursuit/name/<name>', methods=['GET'])
def getDailyFursuitByNameimg(name): # get方式请求
    data = json.loads(DailyFursuitByName(name))
    return "<img src='"+data['data']['url']+"'>"
@app.route('/getimg/DailyFursuit/id/<furid>', methods=['GET'])
def getDailyFursuitByIDimg(furid): # get方式请求
    data = json.loads(DailyFursuitByID(furid))
    return "<img src='"+data['data']['url']+"'>"
@app.errorhandler(KeyError)
def KeyError_error(e):
    return {'code':403,'message':'传参错误，请检查传参'}
config = ConfigParser()
config.read('./config/main.conf', encoding='UTF-8')
app.debug = config['flaskconf']['debug']
ip=config['flaskconf']['blind']
port=config['flaskconf']['port']
app.run(ip, int(port))

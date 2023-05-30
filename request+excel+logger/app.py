#-*- coding:utf-8 -*-

__author__ = "苦叶子"

from doctest import FAIL_FAST
from sre_constants import SUCCESS
from flask import Flask
from flask import jsonify
from flask import request, Response
import random 
import time

app = Flask(__name__)

"""
    这里所有的接口我们才去返回json串
    所有的json传对应的value值都为随机的
"""

# 生成随机字符串
def random_str():
    # 待选随机数据
    data = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"

    # 用时间来做随机播种
    random.seed(time.time())    

    # 随机选取数据
    sa = []    
    for i in range(8):
        sa.append(random.choice(data))
    salt = ''.join(sa)    
    
    return salt
    
# 构建response
def make_response():
    content = '{"result": "%s", "data": "%s"}' % (random_str(), random_str())
    resp = Response(content)
    resp.headers["Access-Control-Origin"] = '*'

    return resp

username = ''
password = ''
# http GET
@app.route("/query", methods=["GET"])
def query():
    resp = Response('{"code":"success","result": "%s", "data": "%s"}' % (username,password))
    return resp,'200',make_response()

# http POST
@app.route("/update", methods=["POST"])
def update():
    username = request.values.get('username')
    password = request.values.get('password')

    if not username and not password:
        return({"msg":"参数不能为空"})
    elif username:
        return({"msg":"请输入用户名"})
    elif password is None or username.isspace() or len(password) == 0:
        return({"msg":"请输入密码"})
    else:
        resp = Response('{"code":"success","result": "%s", "data": "%s"}' % (username,password))
        return resp

@app.route("/ran",methods=["POST"])
def ran():
    a1 = request.json.get('a')
    b1 = request.json.get('b')
    c1 = request.json.get('c')
    if a1 and b1 and c1:
        res = {'code': 'SUCCESS', 'body':{'a':a1,'b':b1,'c':c1}}
    else:
        res = {'code': 'FAIL', 'meg':'参数不全'} 
    return res

# http delete
@app.route("/delete", methods=["DELETE"])
def delete():
    
    return make_response()

# http head
@app.route("/head", methods=["HEAD"])
def head():
    
    return make_response()   

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=1999)

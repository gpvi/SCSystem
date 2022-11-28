"""
@FileName：login.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/23 20:10\n
"""


from flask import Flask,request,url_for,redirect,send_file
import json
import requests



login = Flask(__name__,template_folder="../static/html")

@login.route("/login",methods= ['POST'])
def func():
    data = request.form
    # print(data)
    # print(data['id'])
    # data = json.loads(data)
    try:
        username = data['id']
        password = data['password']
        print("登录成功！！")
        return send_file("../static/html/myclasses.html")
    except:
        print("error")
        return {"success":0}
    
@login.route("/signin",methods = ['POST'])
def signin():
    data = request.form
    content = {'id':data['id'],'name':data['name'],'sex':data['sex'],'pwd':data['pwd']}




if __name__ == '__main__':
    login.run(port = 9090,debug = True)
    
    
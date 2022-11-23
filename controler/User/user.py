"""
@FileName：user.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/22 9:20\n
"""
from flask import  Flask,request,Blueprint,render_template
from models.user import user

userbp = Blueprint("/",__name__)

@userbp.route("/",methods = ['get'])
def index():
    return render_template("index.html",str = 1)

@userbp.route("/varfy",methods = ['POST'])
def verfy():
    print(1)
    varfyJson = request.get_json()
    varfydic = dict(varfyJson)
    print(varfydic)
    # return  "hello"
    p = "no"
    if varfydic['id'] == "admin":
        pass
    else:
        a = user(varfydic)
        a.getdata()
        if a.verify() == True:
            p = "OK"
        else:
            p = "Error"

    return  p;



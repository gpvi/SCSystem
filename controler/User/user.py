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
    return render_template("index.html")

@userbp.route("/verfy",methods = ['post'])
def verfy():
    varfyJson = request.get_json()
    varfydic = dict(varfyJson)
    if varfydic['id'] == "admin":
        pass
    else:
        p  = ""
        a = user(varfydic)
        if a == True:
            p = "OK"
        else:
            p = "Error"

        return render_template("index.html",data = p)



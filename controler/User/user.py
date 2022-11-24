"""
@FileName：User.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/22 9:20\n
"""
from flask import  Flask,request,Blueprint,render_template
from models.User import user

userbp = Blueprint("/",__name__)

@userbp.route("/",methods = ['get'])
def index():
    return render_template("index.html",str = 1)

@userbp.route("/varfy",methods = ['POST'])
def verfy():


#学生主页
@userbp.route("/student")
def stu_index():
    pass

#学生查询选课结果
@userbp.route("/student/get")
def stu_sc_result():

    pass
#查询所有课程
@userbp.route("/student/getall")
def get_all_class():
    pass






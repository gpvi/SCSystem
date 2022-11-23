"""
@FileName：student.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/22 0:19\n
"""
from flask import Flask,Blueprint,request
from models.Student import Student
import json

bpstudent = Blueprint("/user",__name__)

@bpstudent.route("/post",methods = ['post'])
def getdata():
    data_json = request.json()
    stu_dic = dict(data_json)
    stu = Student(stu_dic)
    return stu.getstudent()


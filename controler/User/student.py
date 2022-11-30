"""
@FileName：student.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/22 0:19\n
"""
from flask import Flask,Blueprint,request
from models.Student import Student
import json

bpstudent = Blueprint("/student",__name__)

@bpstudent.route("/mydata",methods = ['get'])
def getdata():
    return "pk"
    return


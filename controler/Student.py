"""
@FileName：Student.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/21 18:13\n
"""
from flask import  Flask,Blueprint,request
from models.Student import  Student

student = Blueprint("/student",__name__)

@student.route("/add",methonds = ['post'])
def addStudent():
    dic = request.get_json()
    dic = dict(dic)

    stu = Student(dic)

    stu.add()




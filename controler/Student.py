"""
@FileName：Student.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/21 18:13\n
"""
from flask import  Flask,Blueprint

student = Blueprint("/student",__name__)

@student.route("/add",methonds = ['post'])
def addStudent():


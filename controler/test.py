"""
@FileName：test.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/30 16:12\n
"""
from  flask import  Flask,Blueprint

a = Blueprint("a",__name__)

@a.route("/a")
def p():
    return  "ok";
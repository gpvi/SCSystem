"""
@FileName：main.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/22 11:14\n
"""

from flask import Flask,request,render_template
from os import urandom
from  controler.login import bplogin
from  controler.User.user import bpuser
app = Flask(__name__)
app.secret_key = urandom(24)
app.register_blueprint(bplogin)
app.register_blueprint(bpuser)


if __name__ == '__main__':
    app.run(port = 9090,debug = True)
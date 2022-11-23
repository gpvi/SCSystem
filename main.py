"""
@FileName：main.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/22 11:14\n
"""

from flask import  Flask,request,render_template

from controler.User.user import userbp

app = Flask(__name__,template_folder="template")

app.register_blueprint(userbp)


if __name__ == '__main__':
    app.run(port = 9090,debug = True)
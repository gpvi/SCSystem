"""
@FileName：user.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/22 0:19\n
"""
from flask import Flask,Blueprint,request
from flask_cors import CORS
from models.Student import Student
import json

bpuser = Blueprint("user", __name__, template_folder="../static/html",url_prefix="/user")
# bpstudent = Flask(__name__)
CORS(bpuser)
@bpuser.route("/mydata", methods = ['GET'])
def getdata():
    id =  request.cookies.get('id')
    stu = Student(id)
    dic = []
    dic.append(stu.getstudent())
    print(dic)
   # jd = json.dumps(dic)
    return dic

# if __name__ == '__main__':
#     bpstudent.run(port=9090,debug=True)
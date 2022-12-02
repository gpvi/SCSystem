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
from models.SC import SC

bpuser = Blueprint("user", __name__, template_folder="../static/html",url_prefix="/user")
# bpstudent = Flask(__name__)
CORS(bpuser)
@bpuser.route("/mydata", methods = ['GET'])
def getdata():
    try:
        id =  request.cookies.get('id')
    except:
        print("未登录")
    stu = Student(id)
    dic = []
    dic.append(stu.getstudent())
    print(dic)
   # jd = json.dumps(dic)
    return dic
@bpuser.route('/getmysc',methods=['GET'])
def getmysc():
    try:
        sno1 = request.cookies.get('id')
    except Exception as e:
        print(e,"获取cookies失败")
    # sno="0256"
    sc = SC(sno1)
    result = sc.query_own()
    return  result
@bpuser.route('/getallclass',methods=['GET'])
def getall():
    try:
        sno1 = request.cookies.get('id')
    except Exception as e:
        print(e,"查询可选课程失败")
    sc = SC(sno1)
    result= sc.getall_not_chose()
    print(result)
    return result
    # pass

@bpuser.route("/choseclass",methods=['POST'])
def chose():
    sno = request.cookies.get('id')
    data = request.form
    cno = data['cno']
    # print(type(data['cno']))
    # print(sno)
    sc = SC(sno,cno)
    sc.addsc()
    return "ok"

@bpuser.route("/dropclass",methods=['post'])
def dropclass():
    sno = request.cookies.get('id')
    cno = request.form['cno']
    sc = SC(sno,cno)
    f = 0;
    try:
        sc.drop_class()
    except Exception as e:
        print("删除课程失败")
        f = 1;

    return f;

# if __name__ == '__main__':
#     bpstudent.run(port=9090,debug=True)
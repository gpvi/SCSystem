"""
@FileName：getdata.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/14 23:00\n
"""
from flask import Flask,request
import json
from databaseInit import  insertall
app = Flask(__name__)

@app.route("/addStudent",methods = ['POST','PUT'])
def addstudent():
    student = request.get_data()
    student = json.loads(student)
    # 获取参数 转为字典类型
    # print(type(student))
    try:
        insertall.insert_student(student)
    except:
        print("Error")
    print(student)

    return "{'inseert':'ok'}"
@app.route("/addTeacher",methods=['POST','PUT'])
def addteacher():
    teacherJson = request.get_data()
    teacher = json.loads(teacherJson)
    # 获取参数 转为字典类型
    # print(type(student))
    # try:
    #     insertall.insert_teacher(teacher)
    # except:
    #     print("Error")
    teacher["action"] = "insert"
    teacher["status"] = "ok"

    return_json = json.dumps(teacher)


    return return_json

if __name__ == '__main__':
    app.run(port=9090,debug=True)



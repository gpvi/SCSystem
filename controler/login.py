"""
@FileName：login.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/23 20:10\n
"""

from flask import Flask,request,send_file
from models.sign import SignIn


login = Flask(__name__,template_folder="../static/html")

@login.route("/login",methods= ['POST'])
def func():
    data = request.form
    # print(data)
    # print(data['id'])
    # data = json.loads(data)
    try:
        dic = {}
        username = data['id']
        password = data['pwd']
        dic.update({'id':username,'pwd':password})
        print(dic)
        # print("登录成功！！")
        sign = SignIn(dic)
        if sign.sign_up():
            print("SUCESS")
            return send_file("../static/html/myclasses.html")
        else:
            return '密码或用户名错误'
    except Exception as e:
        print("error2",e)
        return {"status": e}
    
@login.route("/signup",methods = ['POST'])
def signin():
    data = request.form
    # content = {'id':data['id'],'name':data['name'],'sex':data['sex'],'pwd':data['pwd']}
    print(data)

    # print(content)
    return send_file("../static/html/login.html")
@login.route("/turnsignup")
def turnsignup():
    return send_file("../static/html/sign_up.html")
if __name__ == '__main__':
    login.run(port = 9090,debug = True)
    
    
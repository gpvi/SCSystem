"""
@FileName：login.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/23 20:10\n
"""

from flask import Flask, request, send_file, session,make_response,render_template,Blueprint
from models.sign import SignIn, SignUp

bplogin = Blueprint('login', __name__, template_folder="../static/html")
# bplogin = Flask(__name__,template_folder="../static/html")

@bplogin.route("/login", methods=['POST'])
def func():
    data = request.form
    try:
        dic = {}
        id = data['id']
        password = data['pwd']
        dic.update({'id': id, 'pwd': password})
        # print(dic)
        print("登录成功！！")
        sign = SignIn(dic)
        if sign.sign_in():
            # #会话开启
            # # session['id'] = sign.id
            print("SUCESS")
            htmlfile = render_template("myclasses.html")
            # print(htmlfile)
            try:
                resp = make_response(htmlfile)
            except Exception as e:
                print(e)
            resp.set_cookie('id',id)
            return resp
            # return send_file("../static/html/myclasses.html")
        else:
            return '密码或用户名错误'
    except Exception as e:
        print("error2", e)
        return {"status": e}


@bplogin.route("/signup", methods=['POST'])
def signup():
    data = request.form
    # content = {'id':data['id'],'name':data['name'],'sex':data['sex'],'pwd':data['pwd']}
    print(data)
    dic = {}
    dic.update({'id': data['id']})
    dic.update({'name': data['name']})
    dic.update({'sex': data['sex']})
    dic.update({'pwd': data['pwd']})
    dic.update({'age': data['age']})
    dic.update({'email': data['email']})
    print(dic)
    signup = SignUp(dic)
    signup.insert_db()
    # print(content)
    return send_file("../static/html/login.html")


@bplogin.route("/turnsignup")
def turnsignup():
    return send_file("../static/html/sign_up.html")


# if __name__ == '__main__':
#     bplogin.run(port=9090, debug=True)

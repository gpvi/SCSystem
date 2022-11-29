"""
@FileName：sign.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/28 8:47\n
"""
from sqlconnect import db
import pymysql

class SignIn:
    def __init__(self,dic):
        self.id = dic['id']
        self.pwd = dic['pwd']
    def sign_up(self):
        curs = db.cursor()
        sql = """
        select * 
        from users
        where id="%s";
        """ % self.id

        try:
            curs.execute(sql)
            results = curs.fetchall()
            result = results[0]
            password = result[1]
            if self.pwd == password and self.id == result[0]:
                print("ok")
                return True
        except:
            print("error")
            return False

class SignUp:
    pass



# if __name__ == '__main__':
#     dic = {'id':"abq",'pwd':'jxi'}
#     signIn = SignIn(dic)
#     if signIn.sign_up():
#         print('success')
#     else:
#         print('fail')
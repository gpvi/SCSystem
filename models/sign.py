"""
@FileName：sign.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/28 8:47\n
"""
from sqlconnect import db
import pymysql

class SignUp:
    def __init__(self,dic):
        self.name = dic['name']
        self.id = dic['id']
        self.pwd = dic['pwd']
        self.email = dic['email']


    def sign_up(self):
        curs = db.cursor()
        sql = """
        select * 
        from users
        # where id="123";
        """
        try:
            curs.execute(sql)
            results = curs.fetchall()
            print(results)
            for row in results:
                fid = row[0]
                fname = row(1)
                fpwd = row[2]
                femail = row[3]
        except:
            print("error")

class SignIn:
    pass


if __name__ == '__main__':
    dic = {'id':"123",'name':'123','pwd':456,'email':"aaaa"}
    signup = SignUp(dic)

    signup.sign_up()
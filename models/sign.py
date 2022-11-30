"""
@FileName：sign.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/28 8:47\n
"""
from sqlconnect import DB
import pymysql

class SignIn(DB):
    def __init__(self,dic):
        super(SignIn, self).__init__()
        self.id = dic['id']
        self.pwd = dic['pwd']
    def sign_in(self):
        sql = """
        select * 
        from users
        where id="%s";
        """ % self.id
        curs = self.curs
        try:
            curs.execute(sql)
            results = curs.fetchall()
            result = results[0]
            password = result[1]
            if self.pwd == password and self.id == result[0]:
                print("ok")
                return True
        except Exception as e:
            print("error",e)
            return False

class SignUp(DB):
    def __init__(self,dic):
        super().__init__()
        self.id = dic['id']
        self.name = dic['name']
        self.pwd = dic['pwd']
        self.sex = dic['sex']
        self.email = dic['email']
        self.age = dic['age']

    def insert_db(self):
        print("id:",self.id,"\nname:",self.name,"\nsex:",self.sex,"\npwd:",self.pwd)

        #学生信息
        sql = """
        insert into students(sno, sname, ssex, sage, email)
        value ('%s','%s','%s',%d,'%s');
        """%(self.id,self.name,self.sex,int(self.age),self.email)
        sql1 = """
        insert into users(id, password, name) 
        VALUE ('%s','%s','%s');
        """%(self.id,self.pwd,self.name)
        # print(sql,sql1)

        curs = self.curs
        curs.execute(sql)
        curs.execute(sql1)
        self.db.commit()
        # print("ok")
        # 用户信息
    def varfy_exist(self):
        pass

# if __name__ == '__main__':
#     dic = {'id':"abq",'pwd':'jxi'}
#     signIn = SignIn(dic)
#     if signIn.sign_up():
#         print('success')
#     else:
#         print('fail')
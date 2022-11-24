"""
@FileName：User.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/22 0:18\n
"""
import __init__

class User:

    def __init__(self,dic):
        self.id = dic["id"]
        self.pwd = dic['password']

    def getdata(self):

        print(self.pwd, self.id)

    def verify(self):
        pass
        # test code
        # if self.pwd == "u1" and self.id == "u1":
        #     return True
        # else:
        #     return  False
        #调用数据库验证



# if __name__ == '__main__':
#
#      a = {"ID":"admin","password":"admin"}
#      p  = user(a)
#      p.getdata()
#      print(p.verify())
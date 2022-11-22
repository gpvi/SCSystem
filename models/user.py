"""
@FileName：user.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/22 0:18\n
"""
import __init__

class user:

    def __init__(self,dic):
        self.id = dic["ID"]
        self.pwd = dic['password']

    def verify(self):

        if self.pwd == "admin" and self.id == "admin":
            return True
        else:
            return  False

    def getdata(self):

        print(self.pwd,self.id)


# if __name__ == '__main__':
#
#      a = {"ID":"admin","password":"admin"}
#      p  = user(a)
#      p.getdata()
#      print(p.verify())
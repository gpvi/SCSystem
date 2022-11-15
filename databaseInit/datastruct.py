"""
@FileName：datastruct.py.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/13 21:12\n
"""


class student:
    def __init__(self,Sno,Sname,Ssex,Sage,Sdept):
        self.Sno = Sno
        self.Sname = Sname
        self.Ssex = Ssex
        self.Sage = Sage
        self.Sdept = Sdept

class teacher:
    def __init__(self,Tno,Tname,Tage):
        self.Tno = Tno
        self.Tname = Tname
        self.Tage = Tage


class course:
    def __init__(self,cno,cname,cpno,credit,chours):
        self.Cno = cno
        self.Cname = cname
        self.Cpno = cpno
        self.Credit = credit
        self.Chours = chours


class sc:
    def __init__(self,Sno,Cno,Grade):
        self.Sno = Sno
        self.Cno = Cno
        self.Grade = Grade


class tc:
    def __init__(self,Tno,Cno,Textbook,Cplace,Ctime):
        self.Tno = Tno
        self.Cno = Cno
        self.Textbook = Textbook
        self.Cplace = Cplace
        self.Ctime = Ctime

class user():
    def __init__(self,user_name,pwd):
        self.name = user_name
        self.pwd = pwd


class admin:
    def  __init__(self,type,name,pwd):
        type = "admin"
        self.name = name
        self.pwd = pwd






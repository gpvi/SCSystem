"""
@FileName：Teacher.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/22 0:17\n
"""
from sqlconnect import DB
class Teacher(DB):

    def __init__(self,tno,tname='',tsex='',email="",tage=""):
        super(Teacher, self).__init__()
        self.tno = tno
        self.tname = tname
        self.tsex = tsex
        self.email = email
        self.tage = tage


    def add_one(self):
        sql = """
        insert into teachers(tno, tname, tsex, email, tage) 
        VALUES ('%s','%s','%s','%s','%s')
        """%(self.tno,self.tname,self.tsex,self.email,self.tage)
        print(sql)
        try:
            self.curs.execute(sql)
            self.db.commit()
            return  True
        except Exception as e:
            self.db.rollback()
            print(e,"教师信息插入错误")
            return  False

    def query_one(self):
        sql = """
        select * from teachers
        where Tno = %s       
        """%(self.tno)
        try:
            self.curs.execute(sql)
            result = self.curs.fetchall()
        except Exception as e:

            print(e,"教师信息查询错误")
        #返回嵌套元组
        return result

# if __name__ == '__main__':




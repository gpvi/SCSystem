"""
@FileName：SC.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/22 0:12\n
"""
from sqlconnect import DB
class SC(DB):
    def __init__(self,sno='',cno='',grade=""):
        super(SC, self).__init__()
        self.sno = sno
        self.cno = cno
        self.grade = grade
    #增加一名学生的一个课程
    def addsc(self):
        sql = """
        insert into sc(sno, cno,grade) 
        VALUES (%s,%s,%s)
        """%(self.sno,self.cno,self.grade)
        try:
            self.curs.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e,"1")
        return True

    #设置一个人的一门课成绩
    def set_grade(self,grade_dict):
        sql = """
        update sc
        set grade = %s
        where sno =%s and cno = %s        
        """%(grade_dict["grade"],grade_dict["sno"],grade_dict["cno"])

        try:
            self.curs.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(e,"2")
    #查询一个人的全部课程信息
    def queryall(self):
        sno =self.sno
        sql = """
        select * 
        from query_sc
        where sno= %s
        """%(sno)

        self.curs.execute(sql)
        result = self.curs.fetchall()
        return result

##测试
if __name__ == '__main__':

    sc = SC('0256')
    r = sc.queryall()
    print(r)





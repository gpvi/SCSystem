"""
@FileName：TC.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/22 0:18\n
"""
from  sqlconnect import DB

class TC(DB):
    def __init__(self,tno="",cno="",time="",book=''):
        super(TC, self).__init__()
        self.tno = tno
        self.con = cno
        self.time = time
        self.book = book

    def add_one_tc(self):
        sql="""
        insert into tc(tno, cno, time, textbook) 
        VALUES('%s','%s','%s','%s') 
        
        """%(self.tno,self.con,self.time,self.book)
        try:
            self.curs.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e,"tc插入失败")

    def query_tc_t(self):
        sql = """
        select * from tc
        where tno='%s'
        """%(self.tno)
        try:
            self.curs.execute(sql)
            result = self.curs.fetchall()
        except Exception as e:
            self.db.rollback()
            print(e,"tc查询错误")

if __name__ == '__main__':
    tno = ['1','10']
    cno = ['1','2','3','4','5']
    for i in tno:
        c = 0
        for j in cno:
            b = "b"+str(c)
            c = c+1
            tc = TC(i,j,book=b)
            tc.add_one_tc()


"""
@FileName：SC.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/22 0:12\n
"""
from sqlconnect import DB
class SC(DB):



    def __init__(self,sno,cno,tno):
        super(SC, self).__init__()
        self.sno = sno
        self.cno = cno
        self.tno = tno

    def listup(self,sno,list_cno):
        tuplist = []
        for i in range(0,len(list_cno)):
            temp = tuple(sno,list_cno[i])
            tuplist.append(temp)
        return tuplist

    def addsc(self):
        sql = """
        insert into sc(sno, cno) 
        VALUES (%s %s)
        """
        try:
            self.curs.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)



    def set_grade(self):
        sql = """
        update sc
        set grade = %s
        where sno =%s and cno = %s        
        """




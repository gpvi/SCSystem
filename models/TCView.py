"""
@FileName：TCView.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/22 0:18\n
"""
from  sqlconnect import DB

class TC(DB):
    def __init__(self,sno):
        super(TC, self).__init__()
        self.sno = sno
    def one_sc(self):
        sql = """
        select * 
        from sc
        where sno ="%s"
        """%(self.sno)
        self.curs.execute(sql)
        self.db.commit()


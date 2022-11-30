"""
@FileName：Student.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/21 18:30\n
"""
from sqlconnect import DB
class Student(DB):
    def __init__(self,sno):
        super().__init__()
        self.Sno = sno
        self.Sname = ""
        self.Sage = ""
        self.Ssex = ""
        self.email= ""

    def getstudent(self):
        sql = """
         select *
         from students
         where sno = '%s';
        """%(self.Sno)
        self.curs.execute(sql)
        data = self.curs.fetchall()
        # self.db.commit()
        # self.Ssex=data[0][]
        print(data)
    def deleteStudent(self):
        sql = """
        
        """

    def updataStudent(self):
        sql = """
        
        """
if __name__ == '__main__':
    a = Student("00123")
    a.getstudent()

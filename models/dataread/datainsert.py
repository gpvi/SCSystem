"""
@FileName：datainsert.py.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/12/1 0:45\n
"""
from sqlconnect import DB
from read import Read

Db = DB()
db =Db.db
curs = Db.curs
read = Read()
read.run()
print(read.courses)

def listtup(dic):
    lis = []
    for i in dic:
        lis.append(tuple(i.values()))
    return lis


def insert_stu():
    sql = """
    insert into students(sno, sname, ssex, sage, email) 
    VALUES (%s,%s,%s,%s,%s)
    """
    stus = read.stus
    print(stus)
    list_tup = listtup(stus)
    # print(list_tup)
    # for i in stus:
    #     tup = tuple(i.values())
    #     print(tup)
    #     curs.executemany(sql,tup)
    curs.executemany(sql,list_tup)
    db.commit()

def insert_teachers():
    sql = """
      insert into teachers(tno, tname, tsex, email, tage) 
      VALUES (%s,%s,%s,%s,%s)
      """
    teachers = read.teachers
    print(teachers)
    list_tup = listtup(teachers)
    # print(list_tup)
    # for i in stus:
    #     tup = tuple(i.values())
    #     print(tup)
    #     curs.executemany(sql,tup)
    curs.executemany(sql, list_tup)
    db.commit()

def insert_course():
    sql = """
        insert into courses(cno, cname, cmaxnum, cleftnum, credit, chours) 
        VALUES (%s,%s,%s,%s,%s,%s)
        """
    courses = read.courses
    print(courses)
    list_tup = listtup(courses)
    # print(list_tup)
    # for i in stus:
    #     tup = tuple(i.values())
    #     print(tup)
    #     curs.executemany(sql,tup)
    curs.executemany(sql, list_tup)
    db.commit()
if __name__ == '__main__':
    # insert_stu()
    # insert_teachers()
    insert_course()
    # pass
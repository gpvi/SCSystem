# encoding:utf-8
import pymysql,json
db = pymysql.connect(host="localhost", user= "root", password="123456",database="SCDB")
cursor = db.cursor()

def submit(sql):
    result = ''
    try:
        result = cursor.execute(sql)
        db.commit()
        print(1)
    except:
        db.rollback()
    finally:
        print(result)
def insert_student(student):
        #插入学生信息

        result = 0
        sql1 = """
        insert into students(sno, sname, ssex, sage, sdept)
        VALUES ('%s','%s','%s',%d,'%s');
        """ %((student["Sno"]),(student["Sname"]),(student["Ssex"]),student["Sage"],student["Sdept"])
        submit(sql1)

def insert_teacher():
    teacher = {"Tno":"testno","Tname": "testname","Tage":6}
    result = 0
    sql  = """
    insert into teachers(tno, tname, tage) 
    VALUES ('%s','%s',%d)
    """%(teacher["Tno"],teacher["Tname"],teacher["Tage"])
    submit(sql)


def insert_course(course):
    course = {"Cno": "tno", "Cname": "testname", "Cpno": "math","Credit":5,"Chours":9}
    result = 0
    sql = """
        INSERT INTO scdb.courses (Cno, Cname, Cpno, Credit, Chours) 
        VALUES ('%s', '%s', '%s', %d, %d)
        """ % (course["Cno"],course["Cname"],course["Cpno"],course["Credit"],course["Chours"])

    submit(sql)




# if __name__ == '__main__':
#
#     student = {}
    # insert_student()
    # insert_teacher()
    # # insert_course()
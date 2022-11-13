# encoding:utf-8
import pymysql

student = {"Sno":"0","sname":"root","ssex":"男","Sage":18,"Sdept":"CS"}
#插入学生信息
sql1 = """

insert into students(sno, sname, ssex, sage, sdept)
VALUES ("%s","%s","%s",%d,"%s");
""" %(student["Sno"],student["sname"],student["ssex"],student["Sage"],student["Sage"])

print(sql1)
#插入教师信息


#插入课程信息


#插入选课信息


#插入授课信息
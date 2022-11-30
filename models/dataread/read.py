

import numpy as np
import pandas as pd



class Read:
    def __init__(self,path ="sc.xlsx"):
        self.path = path
        self.stu = pd.read_excel(self.path,sheet_name="stu")
        self.course = pd.read_excel(self.path,sheet_name="course")
        self.teacher = pd.read_excel(self.path,sheet_name="teacher")
        self.stus = []
        self.teachers = []
        self.courses = []
        
    def read_stu(self):
        stu = self.stu
        stus = []
        l = len(stu.columns.values)
        cname = stu.columns.values
        for i in range(0,len(stu)):
            temp= {}
            for j in range(0,5):
                if j == 0:
                    st= str(int(stu.iloc[i][j]))
                else:
                    st = stu.iloc[i][j]
                temp.update({cname[j]:st})
                # print(type(cname[j]))
            stus.append(temp)
        self.stus = stus
            # print(stus)
            


    def read_teacher(self):
        teacher = self.teacher
        teachers = []
        cname = teacher.columns.values
        l= len(teacher.columns.values)
        for i in range(0,len(teacher)):
            temp= {}
            for j in range(0,5):
                if j == 0:
                    st= str(int(teacher.iloc[i][j]))
                else:
                    st = teacher.iloc[i][j]
                temp.update({cname[j]:st})
                # print(type(cname[j]))
            teachers.append(temp)
        # print(teachers)
        self.teachers = teachers

# print(stu.columns.values)
# print(course.columns.values)
# print(len(teacher.columns.values))
# print(teacher.dtypes)

    def read_course(self):
        course = self.course
        courses = []
        cname = course.columns.values
        l= len(course.columns.values)
        for i in range(0,len(course)):
            temp = {}
            for j in range(0,6):
                if j == 0:
                    st= str(int(course.iloc[i][j]))
                else:
                    st = course.iloc[i][j]

                temp.update({cname[j]:st})
                # print(type(cname[j]))
            courses.append(temp)
        self.courses = courses
        # print(self.courses)

        # print(courses)
    
    def run(self):
        self.read_stu()
        self.read_teacher()
        self.read_course()
        # print(self.courses)
        # print(self.course)
        # print(self.stus)
        # print(self.teachers)
#
# if __name__ == '__main__':
#
#     red = Read()
#     red.run()





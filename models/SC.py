"""
@FileName：SC.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/22 0:12\n
"""
from sqlconnect import DB
import re


class SC(DB):
    def __init__(self, sno='', cno='', grade="", tno=""):
        super(SC, self).__init__()
        self.sno = sno
        self.cno = cno
        self.tno = tno
        self.grade = grade

    # 增加一名学生的一个课程
    def addsc(self):
        sql = """
        insert into sc(sno, cno,grade) 
        VALUES ('%s','%s','%s')
        """ % (self.sno, self.cno, self.grade)
        try:
            self.curs.execute(sql)
            self.db.commit()

        except Exception as e:
            self.db.rollback()
            print(e, "1")

        return True

    # 设置一个人的一门课成绩
    def set_grade(self, grade_dict):
        sql = """
        update sc
        set grade = %s
        where sno =%s and cno = %s        
        """ % (grade_dict["grade"], grade_dict["sno"], grade_dict["cno"])

        try:
            self.curs.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(e, "2")


    # 查询一个人的全部课程信息
    def queryall(self):
        sno = self.sno
        sql = """
        select sno, cno, cname, cmaxnum, cleftnum, credit, chours, time, textbook, tname
        from query_sc
        where sno= %s
        """ % sno

        self.curs.execute(sql)
        result = self.curs.fetchall()

        return result

    def query_own(self):
        no = self.sno
        # no='0256'
        sql = """
               select sno, cno,cname,  credit, grade, chours, tname,textbook,time
               from for_own_query
               where sno= '%s'
               """ % no

        self.curs.execute(sql)
        result = self.curs.fetchall()
        list_result = []
        for item in result:
            temp = {'cno':item[1],'cname': item[2], 'credit': item[3], 'grade': item[4],'chours': item[5], 'tname': item[6],
                    'book':item[7],'time': item[8],}
            list_result.append(temp)

        return list_result

# -------------------------------------
# --------------------------------------
#找出登录用户的待选课程
    def getall_not_chose(self):
        l1 = self.notchose(self.sno)
        result = self.notchose_data(l1)
        list_result=[]
        # print(result)
        cid = []
        for item in result:
            temp = {'cid':item[0],'cname': item[1], 'credit': item[4] , 'chours': item[5],'tname': item[8], 'maxnum':item[2],
                    'leftnum': item[3],'time':item[6]}
            list_result.append(temp)
            cid.append(temp['cid'])
        # print("最终待选课程:",cid)

        return  list_result

    def tuplist_to_list(self,tups):
        lis = []
        for item in tups:
            lis.append(str(item[0]))
        return lis

# 找到某位学生没选的课程号
    def notchose(self,sno):
    #------------------------------
        #找出未选的课，包括相同课程
        sql = """
        select cno from tc
        where cno not in
        (select cno from sc  
        where sno='%s');
        """% sno
        self.curs.execute(sql)
        result1 = self.curs.fetchall()
        r1list = self.tuplist_to_list(result1)
        # print("初始未选课程：",r1list)

    #------------------------------
        # 找出已选的课程
        sql2 = """
        select cno from sc
        """
        self.curs.execute(sql2)
        result2= self.curs.fetchall()
        r2list = self.tuplist_to_list(result2)
        # print("r2list:",r2list)
        # print(r2list[0][:-1])
    #-----------------------
        #获取正则匹配模板字符串
        pattlist = []
        for i in r2list:
            pattlist.append(i[:-1])
        # print(pattlist)
        #构建待验证字典
        datadic = {}
        for i in r1list:
            datadic.update({i:0})
        # print(datadic,"-----------------")
        #正则匹配找出没选的课程
        resultset = set()
        for item1 in pattlist:
            for item2 in r1list:
                f = re.search(str(item1),str(item2))
                if f !=None:
                    datadic[item2]=1

        # print(datadic)
        finallist = []
        for k,v in datadic.items():
            if v==0:
                finallist.append(k)
        # print("最终待选：",finallist)


        return finallist

#基于课程号列表，找到所有课程信息
    def notchose_data(self,cno_list):
        result =[]
        for  i in cno_list:
            sql = """
                    select  *
                    from courses_chose
                    where Cno = '%s'
                    """% i
            self.curs.execute(sql)
            temp = self.curs.fetchall()
            # print(temp)
            result.append(temp[0])
        # print(result)

        return result

##--------------------------------
#--------------------------------
#退选课程
    def drop_class(self):
        sql = """
        delete
        from sc
        where sno='%s'and cno='%s';
        """% (self.sno,self.cno)

        try:
            self.curs.execute(sql)
            self.db.commit()

        except Exception as e:
            print(e,"退课错误")
            self.db.rollback()

# # # # 测试
if __name__ == '__main__':
#
    sc = SC('0256','1020')
    l = sc.query_own()
    print(l)
#     l =sc.getall_not_chose()
    # print(l)
    # l = sc.notchose()
    # # print(r)
    # print(sc.notchose_data(l))


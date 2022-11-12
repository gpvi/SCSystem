import pymysql


db = pymysql.connect(
    host='localhost',
    user = 'root',
    password='123456',
    database='library')


#创建游标
cursor = db.cursor()
#仓库表
create_table_respority = """
CREATE TABLE  if not exists repertory(

`BookISBNId`  char(80) NOT NULL ,

`Stock`  int NOT NULL ,

`BookName`  char(30) NOT NULL ,

`FloorNum`  int NOT NULL ,

PRIMARY KEY (`BookISBNId`, `Stock`)
)
;
"""
#订单表
create_table_order = """

CREATE TABLE orders(
 
`OrderID`  char(80) NOT NULL ,
 
`OrderCusNickname`  char(20) NOT NULL ,
 
`OrderCusName`  char(20) NOT NULL ,
 
`OrderData`  datetime NOT NULL ,
 
`OrderBook`  char(30) NOT NULL ,
 
`OrderCount`  int NOT NULL ,
 
`OrderSendData`  datetime NOT NULL ,
 
PRIMARY KEY (`OrderID`, `OrderCusNickname`)
);
"""
#管理员表
create_table_manager ="""
CREATE TABLE managerinfo (
 
`ManaID`  char(30) NOT NULL ,
 
`ManaName`  char(20) NOT NULL ,
 
`ManaPasswd`  char(30) NOT NULL ,
 
`ManaIden`  char(20) NOT NULL ,
 
`ManaMail`  char(20) NOT NULL ,
 
PRIMARY KEY (`ManaID`)
 
);"""
#图书类型表
create_table_booktype = """
CREATE TABLE booktypeinfo (
 
`BookClass`  char(20) NOT NULL ,
 
`BookClassName`  char(20) NOT NULL ,
 
PRIMARY KEY (`BookClass`)
 
);
"""

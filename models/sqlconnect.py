"""
@FileName：sqlconnect.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/23 19:56\n
"""
import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='scdb1')

"""
@FileName：sqlop.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/23 19:45\n
"""

import pymysql
from sqlconnect import db
def conducted(sql_str):
    cursor = db.cursor()
    try:
        cursor.execute(sql_str)
    except pymysql.err.OperationalError as e:
        print(e.args)
    cursor.execute(sql_str)
    db.commit()


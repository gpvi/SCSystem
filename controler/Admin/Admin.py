"""
@FileName：Admin.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/24 14:14\n
"""

from flask import Blueprint,request


adminbp = Blueprint("/admin",__name__)

@adminbp.route('/add')
def add():
    request.get_json()
    




# @adminbp.route("/del")
#
# @adminbp.route("update")
#
# @adminbp.route("get")


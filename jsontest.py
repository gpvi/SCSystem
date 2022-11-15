"""
@FileName：jsontest.py\n
@Description：\n
@Author：NZQ\n
@Time：2022/11/14 22:49\n
"""
import json
website_info='{"name" : "c语言中文网","PV" : "50万","UV" : "20万","create_time" : "2010年"}'

t = json.loads(website_info)

print(type(t))

# coding:utf-8
import json
from pymongo import MongoClient

client = MongoClient(host='127.0.0.1', port=27017)

db = client.demo

db.authenticate('zhou','1234')

collection = db.movie

# 数据库查找find_one() 返回一个字典
# 不指定参数默认返回第一条数据
m = collection.find_one(projection={"title":True,"director_name":True})
print(m)
print(m.get('title'))


""" 通过projection控制返回的字段 """
# 当指定参数时返回匹配条件的第一条数据
# {"title":True,"director_name":True}
# 表示只返回这两个字段的值
# _id字段会默认返回
# 如果不想要_id字段，我们可以指明
m = collection.find_one({'title_year':2015},projection={"title":True,"director_name":True})
print(m)
# {'_id': ObjectId('61bf303a65163952340c0dfa'), 'title': 'Spectre', 'director_name': 'Sam Mendes'}
m = collection.find_one({'title_year':2015},projection={"title":True,"director_name":True,"_id":False})
print(m)
# {'title': 'Spectre', 'director_name': 'Sam Mendes'}
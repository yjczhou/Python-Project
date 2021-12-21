# coding:utf-8
import json
from pymongo import MongoClient

client = MongoClient(host='127.0.0.1', port=27017)

db = client.demo

db.authenticate('zhou','1234')

collection = db.movie

# 数据库查找find_one() 返回一个字典
# 不指定参数默认返回第一条数据
m = collection.find_one()
print(m)
print(m.get('title'))
# 当指定参数时返回匹配条件的第一条数据
m = collection.find_one({'title_year':2015})
print(m)

# 数据库查找find(),返回一个可迭代的对象
# ms = collection.find()
# # print(ms)
# for m in ms:
#     print(m)

# 指定参数就返回所有title_year:2015的数据
ms = collection.find({'title_year':2015})
# print(ms)
for m in ms:
    print(m)
    
# 还可以多级过滤
"""  
    假设在mongodb里有这样几条数据
    a={
        "a":{"key":1},
        "b":1
    }
    b = {
        "a":{"key":2}
    }
    c={
        "a":{"key":1,"v":2}
    }
    collection.find({'a.key':1})
    过滤出所有a的value的 “key”的value 为1的记录
"""
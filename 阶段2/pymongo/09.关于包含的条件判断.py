# coding:utf-8

# 导入模块
# DESCENDING 是处理降序的 在sort()里面可以使用
from pymongo import MongoClient, DESCENDING

# 创建连接
client = MongoClient(host='127.0.0.1', port=27017)

# 指定连接数据库
db = client.demo

# 验证用户信息
db.authenticate('zhou','1234')

# 指定连接集合
collection = db.movie

''' $ne（not equal）不等于  $in包含  $nin（not in）不包含'''


# 查询国家不等于USA的国家
# m_list =  collection.find({'country':{"$ne":"USA"}})
# for m in m_list:
#     print(m)
    

# 国家不在usa范围内的
# m_list = collection.find({'country':{"nin":["USA"]}})
# for m in m_list:
#     print(m)

# 国家在uk,usa范围内的
m_list = collection.find({'country':{"$in":["USA","UK"]}})
for m in m_list:
    print(m)
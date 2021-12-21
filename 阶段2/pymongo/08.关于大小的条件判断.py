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

'''$lt小于 $gt大于 $lte小于等于 $gte大于等于'''

# 查找评分是7分的
m_list = collection.find({"imdb_score":7})
for i in m_list:
    print(i)
    
#查找评分小于等于7分的 {"imdb_score":{"$lte":7}}
m_list = collection.find({"imdb_score":{"$lte":7}})
for m in m_list:
    print(m)

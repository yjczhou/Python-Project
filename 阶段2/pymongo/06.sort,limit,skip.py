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

""" sort排序   limit限制返回结果   skip 跳过多少条数据 """

# 返回所有结果，是一个可迭代的数据
movies = collection.find()
# 按照title_year排序,默认升序，
# 如果指定direction = DESCENDING，则为降序排列
# 这个DESCENDING需要从pymongo里面导入
# for m in movies.sort("title_year",direction=DESCENDING):
#     print(m)

# 按照imdb_score排序，
# 降序排列
# 然后通过limit()方法限制返回结果
# for m in movies.sort("imdb_score",DESCENDING).limit(10):
#     print(m)
    
# 还可以实现分页效果
# 跳过前10的数据
for m in movies.sort("imdb_score",DESCENDING).skip(10).limit(10):
    print(m)
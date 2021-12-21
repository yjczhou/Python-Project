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
collection = db.test

# 插入多条数据
# collection.insert_many([
#     {"x":1,"y":1},
#     {"x":2,"y":2},
#     {"x":3,"y":3},
#     {"x":4,"y":4},
#     {"x":5,"y":5},
# ])

'''update_one()更新一条数据'''
# update_one(filter,update)
# $set是指对哪个或那几个字段进行更新，如下面代码是更新y字段
# 根据{"x":1}，对对应数据的{"$set":{"y":10}}字段进行更新
collection.update_one({"x":1},{"$set":{"y":10}})
collection.update_one({"x":2},{"$set":{"y":10,"z":20}})

# 如果我们根据查找的条件找不到数据，默认不会添加到数据库中
# 但是如果我们加了一个upsert = True,就会添加到数据库中
collection.update_one({"x":11},{"$set":{"y":10,"z":20}},upsert=True)


'''update_many()更新多条数据'''
# update_many(filter,update)
# 如果filter={}，代表更新所有数据
# 把所有数据的y变成100
collection.update_many({},{"$set":{"y":100}}) 
# 如果我们根据查找的条件找不到数据，默认不会添加到数据库中
# 但是如果我们加了一个upsert = True,就会添加到数据库中
collection.update_many({"x":12},{"$set":{"y":100}},upsert = True)
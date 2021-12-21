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
# 如果test集合里面有数据会把里面的数据删除掉
collection.drop()

# 插入多条数据
collection.insert_many([
    {"x":1,"y":1},
    {"x":2,"y":2},
    {"x":3,"y":3},
    {"x":4,"y":4},
    {"x":5,"y":5},
])

'''delete_one()删除一条数据 返回删除的数量'''
# result = collection.delete_one({"x":1})
# # 得到删除的数量
# print(result.deleted_count)
# for item in collection.find():
#     print(item)
# # 如果已经没有了要删除的数据，是不会执行的
# collection.delete_one({"x":1})

'''delete_many()删除多条数据 返回删除的数量'''
# 表示删除x:1,x:2，x:3的数据
result = collection.delete_many({"x":{"$in": [1,2,3]}})
print(result.deleted_count)
for item in collection.find():
    print(item)
from pymongo import MongoClient

# 实例化一个client对象
# 如果不填参数，会默认连接本地的127.0.0.0 端口27017
client = MongoClient(host = '127.0.0.1',port=27017)

# 打印数据库信息
print(client.server_info())


# 使用demo数据库
# use demo
# 代表连接到demo数据库
# 现在知识初始化，还没有真正连接
db = client.demo
# 验证
db.authenticate('zhou','1234')
print(db)
# Database(MongoClient(host=['127.0.0.1:27017'], 
# document_class=dict,
# tz_aware=False, connect=True), 'demo')

# 代表连接到demo数据库下的movie集合
# 以下两种方法都行
collection = db.movie
# collection = db['movie']
print(collection)
# Collection(Database(MongoClient(host=['127.0.0.1:27017'], 
# document_class=dict, tz_aware=False, connect=True), 'demo'), 'movie')
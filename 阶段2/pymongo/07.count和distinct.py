# coding:utf-8

'''count 和distinct'''

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

'''count()计算结果的数量'''
# ! count is deprecated. Use Collection.count_documents instead.
# count()方法已经被替代了，使用count_documents()
print(collection.find().count())
# 需要有一个过滤参数，没有过滤参数也需要填一个空大括号
print(collection.count_documents({"title_year":2015}))
print(collection.count_documents({}))



'''distinct() 判断某一个字段有多少不同值 返回一个列表'''

print(collection.find().distinct('director_name'))
# ['Andrew Adamson', 'Andrew Stanton', 'Anthony Russo', 'Barry Sonnenfeld', 'Baz Luhrmann', 'Brad Bird', 'Brett Ratner', 'Bryan Singer', 'Carl Rinsch', 'Chris Weitz', 'Christopher Nolan', 'Colin Trevorrow', 'Dan Scanlon', 'David Ayer', 
# 'David Yates', 'Dean DeBlois', 'Don Hall', 'Doug Liman', 'Duncan Jones', 'Gore Verbinski', 'Guillermo del Toro', 'J.J. Abrams', 'James Cameron', 'James Gunn', 'James Wan', 'John Lasseter', 'Jon Favreau', 'Jonathan Mostow', 'Joseph Kosinski', 'Joss Whedon', 'Justin Lin', 'Kevin Reynolds', 'Lana Wachowski', 'Lee 
# Unkrich', 'Marc Forster', 'Marc Webb', 'Mark Andrews', 'Martin Campbell', 'Martin Scorsese', 'Matt Reeves', 'Matthew Vaughn', 'McG', 'Michael Bay', 'Mike Mitchell', 'Mike Newell', 'Nathan Greno', 'Pete Docter', 'Peter Berg', 'Peter Jackson', 'Peter Sohn', 'Rich Moore', 'Ridley Scott', 'Rob Cohen', 'Rob Letterman', 'Rob Marshall', 'Robert Stromberg', 'Robert Zemeckis', 'Roland Emmerich', 
# 'Rupert Sanders', 'Sam Mendes', 'Sam Raimi', 'Shane Black', 'Stephen Sommers', 'Steven Spielberg', 'Tim Burton', 'Tom Shadyac', 'Zack Snyder']
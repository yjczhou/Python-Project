# coding:utf-8
import json
from pymongo import MongoClient

client = MongoClient(host='127.0.0.1', port=27017)

db = client.demo

db.authenticate('zhou','1234')

collection = db.movie

with open('./movie.json','r') as f:
    data = json.loads(f.read())
print(type(data))
# print(data)
collection.insert_many(data)

client.close()
from datetime import datetime

import mongoengine

# 嵌入式的Document 对象形式
class Address(mongoengine.EmbeddedDocument):
    city = mongoengine.StringField(required=True)
    zip_code = mongoengine.IntField(required=True)
    # 这里我们没必要用meta
    # 因为这个Address只是User的一个字段值

# 嵌入式Document 对象形式
class Hobby(mongoengine.EmbeddedDocument):
    type = mongoengine.StringField(required=True)
    rating = mongoengine.IntField(default=8)
    


class User(mongoengine.Document):
    # StringField()字符串类型
        # max_length最大长度
        # required = True 表示为必填字段
    username = mongoengine.StringField(max_length=10,min_length=4,required=True)
    password = mongoengine.StringField(max_length=20,min_length=4,required=True)
    email = mongoengine.EmailField(required=True)
    age = mongoengine.IntField(required=True)
    # 时间类型 default默认值
    created_at = mongoengine.DateTimeField(default=datetime.utcnow)
    
    
    # 嵌套的字段 对象形式，如何创建
    # 如
    # {
    #     "address":{
                # "city":"",
                # "zip_code":""
    #               }
    # }
    address = mongoengine.EmbeddedDocumentField(Address, required=True)
    
    # 嵌套的字段 列表形式 复杂的形式 EmbeddedDocumentListField
    # 这里也可以直接使用ListField
    # "hobbies": [
    #     {
    #         "type": "reading",
    #         "rating": 9
    #     },
    #     {
    #         "type": "running",
    #         "rating": 10
    #     }
    # ]
    # 说明hobbies字段的值是一个列表
    hobbies = mongoengine.EmbeddedDocumentListField(Hobby,required=True)
    
    
    
    # User的属性
    meta = {
        # 在main.py中定义
        'db_alias': 'core',
        # 集合名
        'collection': 'users',
        # 默认设置排序，按照age降序
        'ordering': ['-age']
    }

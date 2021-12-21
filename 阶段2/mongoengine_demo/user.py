from datetime import datetime

import mongoengine


class Address(mongoengine.EmbeddedDocument):

    city = mongoengine.StringField(required=True)
    zip_code = mongoengine.IntField(required=True)


class Hobby(mongoengine.EmbeddedDocument):
    type = mongoengine.StringField(required=True)
    rating = mongoengine.IntField(default=8)


class User(mongoengine.Document):
    # 字符串类型
    username = mongoengine.StringField(
        max_length=10, min_length=4, required=True)
    password = mongoengine.StringField(
        max_length=20, min_length=4, required=True)
    email = mongoengine.EmailField(required=True)
    age = mongoengine.IntField(required=True)
    # 时间类型
    created_at = mongoengine.DateTimeField(default=datetime.utcnow)
    address = mongoengine.EmbeddedDocumentField(Address, required=True)
    hobbies = mongoengine.EmbeddedDocumentListField(Hobby, required=True)

    # User的属性
    meta = {
        # 在main.py中定义
        'db_alias': 'core',
        # 集合名
        'collection': 'users',
        'ordering': ['-age']
    }

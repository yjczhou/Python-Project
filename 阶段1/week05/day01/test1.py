# coding:utf-8

# from animal import dog_action
# from animal import cat_action
# 可以简写
from animal import dog_action,cat_action
from animal.cat.action import cat_name

# 如果导入的是一个类
# 可以实例化之后在使用

print(cat_name)
print(dog_action.run())
print(cat_action.run())

def test1():
    return 'test1'
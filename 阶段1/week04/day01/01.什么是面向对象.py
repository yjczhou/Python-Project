# coding:utf-8

'''什么是面向对象编程'''
# 利用（面向）对象（属性和方法）去进行编码的过程
# 自定义对象数据类型就是面向对象中的类（class）的概念

'''类的关键字class'''
# class用来声明类，类的名称首字母大写，多单词情况下每个单词首字母大写

'''类的定义'''
# object代表python中通用对象，在类名后面可以不用写，但python3.0之后建议书写，书写后会带有更多的通用功能
# self一定要写在第一个参数位
# class Name(object):
#   attr = something
#   def fun(self):
#       do

class Person(object):
    # 类属性
    name = '小慕'
    # 类函数
    def dump(self):
        print(f'{self.name} is dumping')
        
        
# 实例化一个类
xiaomu = Person()
print(xiaomu.name)
xiaomu.dump()
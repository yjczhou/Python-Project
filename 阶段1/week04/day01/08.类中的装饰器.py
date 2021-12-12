# coding:utf-8

'''类中的装饰器'''
'''classmethod装饰器的功能'''
# 将 类函数 可以不经过 实例化 而直接调用
'''classmethod装饰器的用法'''
# @classmethod
# def func(cls,...):
#     do
# cls替代普通类函数中的self，变为cls，代表当前操作的是类

# 例子
class Test(object):
    @classmethod
    def add(cls,a,b):
        return a+b
# 类没有实例化二可以直接调用
print(Test.add(1,2))
print('--------------------------------')
'''staticmethod装饰器的功能'''
# 将 类函数可以不经过实例化 而直接被调用，
# 被该装饰器调用的函数 不许 传递self或cls参数，且无法在该函数内调用其他函数或类变量
'''staticmethod装饰器的用法'''
# @staticmethod
# def func(...):
#   do
# 函数体内无cls或self参数

# 例子
class Test2(object):
    
    @staticmethod
    def add(a,b):
        return a+b
print(Test2.add(2,2)) 
print('--------------------------------')

'''property装饰器的功能'''
# 将类函数的执行免去括弧，类似于调用属性（变量）
'''property装饰器的用法'''
# @property
# def func(self):
#   do
# 无重要参数说明

# 例子
class Test3(object):
    def __init__(self,name):
        self.name = name
    
    @property
    def call_name(self):
        return 'hello {}'.format(self.name)
test = Test3('小慕')
# 使用效果
result = test.call_name
print(result)
print('--------------------------------')

class Test4(object):
    def __init__(self,name):
        self.__name = name
    
    @property
    def call_name(self):
        return self.__name
    
    # property装饰器如何给函数传参呢？
    @call_name.setter
    def call_name(self,value):
        self.__name = value
        
test = Test4(name='dewei')
# property装饰器之后的方法调用   
print('名字为',test.call_name)   
#property的修改参数办法
test.name = 'xiaomu'  
print('修改之后名字为',test.call_name) 
print('--------------------------------')

# 案例
class Test1(object):
    def __init__(self,a):
        self.a=a
    
    def run(self):
        print('run')
        # 但是可以在需要self的函数中调用需要cls的函数
        # 在self中可以调用classmethod装饰器的函数，
        # 也可以调用staticmethod装饰器的函数
        # self.dump() #可以执行
        # self.sleep() #可以执行
    
    @classmethod
    def dump(cls):
        print('dump')   
        # 注意无在cls函数中调用需要self的函数
        # cls.run()# 报错
    
    @staticmethod
    def sleep():
        print('I want sleep')
        
t = Test1('a')
t.run()
# Test1.run() # 报错

# 这个函数绑定了装饰器，可以不用实例化就可以直接使用
Test1.dump()
Test1.sleep()


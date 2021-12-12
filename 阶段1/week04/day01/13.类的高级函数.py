# coding:utf-8

'''类的高级函数'''

'''__str__的功能'''
# 如果定义了该函数，当print当前实例化对象的时候，会返回该函数的return信息
'''__str__的用法'''
# def __str__(self):
#     return str_type
# 返回值： 一般返回对于该类的描述信息

# 例子
class Test(object):
    def __str__(self):
        return '这是关于这个类的描述'

test =Test()
print(test)
print('---------------------------')


'''__getattr__的功能'''
# 当调用的属性或者方法不存在时，会返回该方法定义的信息
'''__getattr__的用法'''
# def __getattr__(self,key):
#     print(something...)
# key: 调用任意不存在的属性名
# 返回值： 可以是任意类型也可以不进行返回

class Test(object):
    def __getattr__(self,key):
        print('这个key：{}不存在'.format(key))
        
test = Test()
test.a # 这个key：a不存在
print('---------------------------')

        
'''__setattr__的功能'''
# 拦截当前类中不存在的属性与值
'''__setattr__的用法'''
def __setattr__(self,key,value):
    self.__dict__[key] = value
# key: 当前的属性名
# value: 当前的参数对应的值
# 无返回值

class Test(object):
    def __setattr__(self,key,value):
        print('key=',key,'value=',value)
        if key not in self.__dict__:
            self.__dict__[key] = value
        print(self.__dict__)

t = Test()
t.name = 'dewei'
t.name
print('---------------------------')

'''__call__的功能'''
# 本质是将 一个类 变成  一个函数
'''__call__的用法'''
def __call__(self,*args, **kwargs):
    print('call will start')
# 参数： 可传任意参数
# 返回值： 与函数情况相同可有可无

class Test(object):
    def __call__(self,**kwargs):
        print('arg is {}'.format(kwargs))

t =Test()
# 将实例化的类变成了函数的形式
t(name = 'dewei')
print('---------------------------')

class Test2(object):
    def __init__(self,attr=''):
        self.__attr = attr
        print('__init__',self.__attr)
    
    def __getattr__(self,key):
        if self.__attr:
            key = '{}.{}'.format(self.__attr,key)
        else:
            key = key
        print(key)
        return Test2(key)
    
    def __call__(self):
        print('key is {}'.format(self.__attr))
t2 = Test2()
t2.a.b.c()
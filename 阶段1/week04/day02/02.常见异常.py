# coding:utf-8

'''
异常名称                说明
Exception           通用异常类型（基类）
ZeroDivisionError   不能整出0
AttributeError      对象没有这个属性
IOError             输入输出操作失败
IndexError          没有当前的索引

KeyError            没有这个键值（key）
NameError           没有这个变量（为初始化对象）
SyntaxError         Python语法错误
SystemError         解释器的系统错误
ValueError          传入的参数错误
'''

class Test(object):
    pass

t = Test()
try:
    t.name #AttributeError
except AttributeError as e:
    print(e)
    
d={'name':'xiaomu'}

try:
    d['age']# KeyError
except KeyError as e:
    print('没有对应的键',e)
    
l = [1,2,3]
try:
    l[5]# IndexError
except IndexError as e:
    print(e)
    
name = 'dewei'
try:
    int(name)# ValueError 
except ValueError as e:
    print(e)
    
def test(a):
    return a
try:
    test()# TypeError
except TypeError as e:
    print(e)
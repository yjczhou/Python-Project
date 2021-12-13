# coding:utf-8

'''自定义异常抛出异常函数--raise'''
# 将信息以报错的形式拋出异常
'''自定义异常抛出异常函数--raise用法'''
# raise 异常类型(message)
# 参数：
#      message：错误信息
# 无返回值
# raise ValueError('主动抛出一个异常')


def test(number):
    if number == 100:
        raise ValueError('number 不可以是100')
    return number

test(50)

def test2(number):
    try:
        return test(number)
    except ValueError as e:
        return e

result = test2(50)
print(result)

def  test3():
    raise 'nihao'
# TypeError: exceptions must derive from BaseException
# test3()
    
def test4(name):
    if name=='dewei':
        raise Exception('dewei不可以被填写')
    return name
# test4('dewei')

'''自定义异常类'''
# 继承基类--Exception
# 在构造函数中定义错误信息

class NewError(Exception):
    def __init__(self,message):
        self.message = message

def test():
    raise NewError('this is a bug')

try:
    test()
except Exception as e:
    print(e)
    
class NumberLimitError(Exception):
    def __init__(self,message):
        self.message = message


class NameLImitError(Exception):
    def __init__(self,message):
        self.message = message

def test5(name):
    if name == 'dewei':
        raise NameLImitError('名字不可以是dewei')
    return name
try:
    test5('dewei')
except Exception as e:
    print(e)   

def test6(number):
    if number > 100:
        raise NumberLimitError('数字不可以大于100')
    return number
try:
    test6(101)
except Exception as e:
    print(e)
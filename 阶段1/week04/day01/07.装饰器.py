# coding:utf-8

'''什么是装饰器'''
# 也是一种函数
# 可以接受函数作为参数
# 可以返回一个函数
# 接受一个函数，内部对齐处理，然后返回一个新函数，动态的增强函数功能
# 将c函数在a函数中执行，在a函数中可以选择执行或不执行c函数，也可以对c函数的结果进行二次加工处理

# 例子
# def a():
#     def b():
#         print('hello')
#     b()
# a()

'''装饰器的定义'''
def out(func_args): #外围函数
    def inter(*args, **kwargs): #内嵌函数
        return func_args(*args,**kwargs)
    return inter # 注意不执行 外围函数返回内嵌函数

'''装饰器的用法'''
#方法1： 将被调用的函数直接作为参数传入装饰器的外围函数括弧
#方法2：jiang装饰器与被调用函数绑定在一起
# @符号+装饰器函数放在被调用函数的上一行，被调用的函数正常定义，只需要直接调用被执行函数即可

def a(func):
    def b(*args, **kwargs):
        return func(*args, **kwargs)
    return b
# 方法1
def c(name):
    print(name)

a(c('dewei')) # dewei
# 方法2
# 绑定装饰器
@a
# 定义被调用函数
def c(name):
    print(name)
# 调用
c('dewei')


# 定义装饰器
def check_str(func):
    print('func:',func)
    def inter(*args, **kwargs):
        print('args:',args,'kwargs:',kwargs)
        result = func(*args, **kwargs)
        if result == 'ok':
            return 'result is %s' % result
        else:
            return 'result is failed %s' % result
    return inter

@check_str
def test(data):
    return data
result = test('no')
print(result)
result = test('ok')
print(result)
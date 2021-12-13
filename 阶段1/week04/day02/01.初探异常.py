# coding:utf-8

'''什么是异常域异常处理'''
# 异常就是错误
# 异常会导致程序崩溃并停止运行
# 能监控并捕获到异常，将异常部位的程序进行修理使得程序继续正常运行

'''异常的语法'''

# try:
    # <代码块1> 被try关键字检查并保护的业务代码
# except <异常类型>:
#   # <代码块2> 代码块1出现错误后执行的代码块

try:
    1/0
except:
    print('0不能被1整除')
    print('程序继续执行')
print('--------------------------------')
def upper(str_data):
    new_str = ''
    try:
        new_str = str_data.upper()
    except:
        print('程序出错了')
    return new_str

result = upper(1)
print('result:',result)
print('--------------------------------')
'''捕获通用异常类型'''
# 无法确定是哪种异常的情况下使用的捕获方法
# try:
    # <代码块>
# except Exception as e:
    # <异常代码块>
def upper(str_data):
    new_str = ''
    try:
        new_str = str_data.upper()
    except Exception as e:
        print('程序出错了:{}'.format(e))
    return new_str

result = upper(1)
print('result:',result)
print('--------------------------------')
'''捕获具体异常'''
# 确定是那种异常的情况下使用的捕获方法
# except <具体的异常类型> as e
try:
    1/0
except ZeroDivisionError as e:
    print(e)
print('--------------------------------')

'''捕获多个异常1'''
# 当except代码块中有多个的时候，当捕获到第一个后，不会继续往下捕获
try:
    print('try start')
    res = 1/0
    print('try finish')
except ZeroDivisionError as e:
    print(e)
except Exception as e: #可以有都多个except
    print('this is a public except, bug is :%s' % e)
print('--------------------------------')
'''捕获多个异常2'''
# 当except代码后边的异常类型使用元组包裹起来，捕获到哪种就抛出哪种
def test1():
    try:
        print('try start')
        print(name)
    except (ZeroDivisionError,NameError) as e:
        print(e) 
test1() 



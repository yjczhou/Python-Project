# coding:utf-8

'''finally的功能'''
# 无论是否发生异常，一定会执行的代码块
# 在函数中，即便在try或except中进行return也依然会执行finally语法块
# try语法至少要伴随except或finally中的一个

'''finally的用法'''
# try:
#     <代码块1>
# except:
#     <代码块2>
# finally:
#     <代码块3>

def test1():
    try:
        1/0
    except Exception as e:
        print(e)
    finally:
        return 'finally'

result = test1()
print(result)
print('---------------------------------------')
def test2():
    try:
        1/0
    except Exception as e:
        print('111')
        return e
    finally:
        print('finally')

result = test2()
print(result)
print('---------------------------------------')
def test3():
    try:
        return 'try'
    except Exception as e:
        print(e)
    finally:
        print('finally test')
result = test3()
print(result)
print('---------------------------------------')
def test4():
    try:
        1/0
    except Exception as e:
        return e
    finally:
        return 'finally'
result = test4()
print(result)
print('---------------------------------------')
def test5():
    try:
        return 'try'
    except Exception as e:
        print('e')
    finally:
        return 'finally'
result = test5()
print(result)
print('---------------------------------------')
def test6():
    try:
        1/0
    finally:
        return 'i am finally'
result = test6()
print(result)
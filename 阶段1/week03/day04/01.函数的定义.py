# coding:utf-8

# 函数的定义
# 将一件事情的步骤封装咱一起并得到最终结果
# 函数名代表了这个函数要做的事情
# 函数体是实现函数功能的流程
# 方法或功能
# 函数可以帮助我们重复使用，通过函数名我们可以知道函数的作用

# 函数的分类
# 内置函数
# 自定义函数

# 通过关键字def 定义函数
# def name(arg...):
#   todo something
#   返回值

def say_hello():
    print('hello xiaomu')
    
say_hello()

# 函数的返回值
# 将函数结果返回的关键字
# return 只能在函数体内使用
# return 支持返回所有的python类型
# 有返回值的函数可以直接赋值给一个变量

def add(a,b):
    c=a+b
    return c
result = add(1,1)#参数按顺序传递
print(result)

# return与print的区别
# print只是单纯的将对象打印，不支持赋值语句
# coding:utf-8

'''python中的高阶函数'''

'''filter功能'''
# 对循环根据过滤条件进行过滤
# 返回迭代器
'''filter使用方法'''
# filter(func,list)
# func: 对list每个item进行条件过滤的定义
# list：需要过滤的列表

# 例子
res = filter(lambda x: x > 1,[0,1,2])
print(res)
# 返回值
# <filter object at 0x063672B0>
for i in res:
    print(i)


print('-------------------------------')
'''map的功能'''
# 对列表中的每个成员是否满足条件返回对应的True与False
'''map使用方法'''
# map(func,list)
# func: 对list每个item进行条件满足的判断
# list：需要过滤的列表

# 例子
res = map(lambda x: x > 1,[0,1,2])
print(res)
# 返回值
# <map object at 0x06367808>
for i in res:
    print(i)


print('-------------------------------')
'''reduce的功能'''
# 对循环前后两个数据进行累加
# 返回的不是迭代器
'''reduce使用方法'''
# from functools import reduce
# reduce(func,list)
# func: 对数据累加的函数
# list：需要处理的列表

# 例子
from functools import reduce
res = reduce(lambda x,y: x+y,[0,1,2])
print(res)
# 返回值
for i in res:
    print(i)
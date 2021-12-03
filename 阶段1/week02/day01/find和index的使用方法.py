# coding:utf-8

# find与index 都是返回你想寻找的成员的位置
# string.find(item) item: 你想查询的元素，返回一个整型   str.find(str, beg=0, end=len(string))
# string.index() item: 你想查询的元素，返回一个整型 或报错
# 字符串里的位置是从左到右，以0开始

print('my name is dewei'.find('e'))
print('my name is dewei'.index('i'))

# 区别
# 如果find找不到元素，会返回-1
# 如果index找不到元素，会导致程序报错

print('my name is dewei'.find('z'))
print('my name is dewei'.index('z'))
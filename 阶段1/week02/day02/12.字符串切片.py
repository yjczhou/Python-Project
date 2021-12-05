# coding:utf-8

# 字符串的索引，与列表的索引是一样的
# 索引规则与列表相同
# 切片和索引的获取与列表相同
name = 'dewei'
print(name[0])
print(name[:2])
# 无法通过索引修改与删除 因为字符串不可修改

# find与index函数
# 获取元素的索引位置
# inttype = string.index(item) item为要查找的元素 ,函数返回索引位置
# inttype = string.find(item) item为要查找的元素 ， 函数返回索引
info = 'my name is dewei'
print(info.index('dewei'))
print(info.find('dewei'))
# find 如果获取不到，返回-1
# index 如果获取不到，直接报错
print(info.index('c'))
print(info.find('c'))
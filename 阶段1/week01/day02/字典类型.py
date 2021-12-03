# coding:utf-8

# 字典是有多个键（key）及其对应的值（value）所组成的一种数据类型

# dict用来代表字典， 并且可以创建一个字典
# 通过{}将一个个key与value存入字典中
a = dict()
a = {}

persion = {'name': 'dewei', 'age': 33}

# key支持字符串，数字，元组但不支持列表
# value支持错you类型
a = {'name': 'dewei', 'age': 30}
b = {1: 'one', 2: 'two'}
c = {(1, 2, 3): [1, 2, 3], (4, 5, 6): [4, 5, 6]}

# 3.7之前字典是无序的，之后是有序的
# 字典中每一个key一定是唯一的

# max min 是看的key，按照字母大小比顺序

# coding:utf-8

'''
集合 set 是一个无序的不重复元素序列
集合常用来对两个列表进行交并差的处理
集合与列表一样，支持所有不可变的数据类型
{'name',1,'xiaomu'}
'''

'''
集合与列表的区别
功能          列表          集合
顺序          有序          无序
内容          可重复         不可重复
功能          用于数据的使用  用于数据的交集并集的获取
索引          有索引         无索引
符号          [][1,2,3]    {}{1，2,3}
'''

'''
集合的创建
通过set函数来创建集合，不能使用{}来创建空集合
a_set = set()           空集合
a_set = set([1,2,3])    传入列表或元组
b_set = {1,2,3}         传入元素
c_set = {}              错误
'''

a = set()
print(a)
print(type(a))
print('---------------------------------')
b = set(['python','django','flask'])
print(b)
print('---------------------------------')
# c = {[1,2,3]} #报错
# c = {{'name':'lisi'}} #报错
c = {(1,2,3),1,'string'}
print(c)
print('---------------------------------')
d = {}
print(d,type(d))
print('---------------------------------')
# 会自动去重
a_list = ['python','django','python','flask']
b_set = set(a_list)
print(b_set)
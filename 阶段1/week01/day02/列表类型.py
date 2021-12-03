# coding:utf-8

# 列表就是队列
# 它是各种数据类型的集合，也是一种数据结构
# 列表是一种有序，且内容可重复的集合类型

# list代表这种类型，也可以用它定义一个列表

names_01 = list(['dewei', 'xiaomu', 'dewei'])
names_02 = ['dewei', 'xiaomu', 'dewei']

print(type(names_01))
print(type(names_02))
# 列表是一个无限制长度的数据结构


# in max min
print( 1 in [1,2,3,4])
print( 10 in [1,2,3,4])
print(max([1,2,3,4]))
print(min([1,2,3,4]))
# max 和 min 在列表中使用的时候，列表中的元素不能是多种类型，
# 如果类型不统一，则会报错
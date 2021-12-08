# coding:utf-8

# 集合的差集 difference()
# a {1,2,3.4}
# b {3,4,5,6}
# a，b两个集合，由所有 属于a但不属于b 的元素组成的集合 叫做a与b的差集
# 所以a的差集为1,2 b的差集为 5,6

# difference()
# 返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合中(方法的参数)中
# a_set.difference(b_set)  b_set：当前集合需要比对的集合
# 返回原始集合相对于对比集合的差集

a_set = {'xiaomu','name','xiaoming'}
b_set = {'xiaoming','xiaogang','xiaohong'}
a_diff = a_set.difference(b_set)
print(a_diff)
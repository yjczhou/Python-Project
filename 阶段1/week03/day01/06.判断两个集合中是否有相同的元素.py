# coding:utf-8

# isdisjoint()
# 判断两个集合是否包含相同的元素，如果没有返回True，否则返回False
# bool = a_set.isdisjoint(b_set) b_set : 与当前集合用来判断的集合
# 返回一个布尔值

a_set = {'xiaomu','name','xiaoming'}
b_set = {'xiaoming','xiaogang','xiaohong'}
result = a_set.isdisjoint(b_set)
print(result)
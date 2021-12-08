# coding:utf-8

# 集合的交集 intersection()
# a {1,2,3.4}
# b {3,4,5,6}
# a，b两个集合分别拥有的相同的元素集，称为a与b的交集

# intersection()
# 返回两个或更多集合中都包含的元素，及交集
# a_set.intersection(b_set...) b_set... :与当前集合对比1个或多个集合
# 返回原始集合与对比集合的交集

a_set = {'xiaomu','name','xiaoming'}
b_set = {'xiaoming','xiaogang','xiaohong'}
a_inter = a_set.intersection(b_set)
print(a_inter)
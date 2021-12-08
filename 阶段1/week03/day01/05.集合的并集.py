# coding:utf-8

# 集合的并集 union()
# a {1,2,3.4}
# b {3,4,5,6}
# a,b两个集合中所有的元素(去掉重复) 即为a与b的并集
# 所以并集为{1,2,3,4,5,6}

# union()
# 返回多个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次
# a_set.union(b_set...)  b_set...  : 与当前集合对比的1或多个集合
# 返回原始集合与对比集合的并集

a_set = {'xiaomu','name','xiaoming'}
b_set = {'xiaoming','xiaogang','xiaohong'}
a_union = a_set.union(b_set)
print(a_union)
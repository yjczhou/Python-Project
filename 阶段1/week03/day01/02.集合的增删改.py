# coding:utf-8

# add()
# 用于集合中添加一个元素，如果集合中已存在该元素则该函数不执行
# set.add(item) item:要添加到集合的元素

# 定义一个空集合
a_set = set()
a_set.add('dewei')
print(a_set)

# update()
# 加入一个新的集合(或列表、元组、字符串)，如集合内的元素在元集合中存在则无视
# set.update(iterable) iterable: 集合，列表元组字符串

# 可以用update代替add功能，因为add每次只能添加一个
a_set.update([3,4,5])
print(a_set)

# remove()
# 将集合中某个元素删除，如元素不存在将会报错
# set.remove(item) item: 当前集合中的一个元素

a_set.remove(3)
print(a_set)

# clear()
# 清空当前集合中的所有元素
# set.clear()
a_set.clear()
print(a_set)

# del删除集合
# 集合没有索引，所以del只能删除集合自身
# 删除后就没有这个集合了

# 集合中重要说明
# 集合无法通过索引获取元素
# 集合无获取元素的任何方法
# 集合知识用来处理列表或元组的一种临时类型，它不适合存储与传输
  

# coding:utf-8

# keys()
# 获取当前字典中所有的键key
# dict.keys() 返回一个key集合的伪列表
# 伪列表不具备列表的所有功能

my_dict = {'name': 'dewei','age':'33'}
print(my_dict.keys())
# 得到的是伪列表 不过我们可以把它转换成列表
key_list = list(my_dict.keys())
print(key_list)


list = []
list.extend(my_dict) # 这样也可以得到key值
print(list)


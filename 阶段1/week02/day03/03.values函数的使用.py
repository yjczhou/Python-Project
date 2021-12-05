# coding:utf-8

# values()
# 获取当前字典中所有键值对的值(value)
# dict.values() 返回一个value集合的伪列表


my_dict = {'name': 'dewei','age':'33'}
print(my_dict.values())
# 得到的是伪列表 不过我们可以把它转换成列表
value_list = list(my_dict.values())
print(value_list)
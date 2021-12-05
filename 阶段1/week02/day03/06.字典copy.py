# coding:utf-8

# copy()
# 将当前字典赋值一个新的字典
# dict.copy() 返回一个内容一模一样的内存地址不同的字典
my_dict = {'name': 'dewei','age':'33'}
new_dict = my_dict.copy()
print(new_dict)
print(id(new_dict)!=id(my_dict))
# coding:utf-8

# clear()
# 情况当前字典中所有的数据
# dict.clear()
my_dict = {'name': 'dewei','age':'33'}
my_dict.clear()
print(my_dict)
print('-----------------------------------------------')

# pop()
# 删除字典中指定的key，并将其结果返回，如果key不存在则报错
# value = dict.pop(key) key 要删除的键 返回被删除的value
my_dict = {'name': 'dewei','age':'33'}
pop_value = my_dict.pop('age')
print(pop_value)
print(my_dict)
print('-----------------------------------------------')
# del
# del dict['name']
my_dict = {'name': 'dewei','age':'33'}
del my_dict['name']
print(my_dict)
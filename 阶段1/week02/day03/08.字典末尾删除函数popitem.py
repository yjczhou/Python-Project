# coding:utf-8

# popitem()
# 删除当前字典里末尾一组键值对，并将其返回
# dict.popitem() 返回被删除的键值对，用元组包裹0索引是key，1索引是value
# 如果字典为空，直接报错
my_dict = {'name': 'dewei','age':'33'}
print(my_dict.popitem())
print(my_dict)

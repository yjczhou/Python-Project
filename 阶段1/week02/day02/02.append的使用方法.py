# coding:utf-8

# append的功能
# 将一个元素添加到当前列表中

# list.append(new_item)  new_item: 添加进列表的新元素
# 注意事项
# 被添加的元素只会被添加到末尾
# append函数是在原有列表的基础上添加，不需要额外添加新的变量
names = ['xiaomu']
print(id(names))
names.append('dewei')
names.append(None)
print(names)
print(id(names))
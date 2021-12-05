# coding:utf-8

# 删除列表中的某个元素
# list.remove(item)  item: 准备删除的列表元素

# 如果找不到要删除的元素，会报错
# 如果被删除的元素有多个，则会删除从左到右的第一个
# remove函数不会返回一个新数组，而是在原先的列表中对元素进行删除

fruits = ['苹果', '西瓜', '水蜜桃','西瓜']
fruits.remove('苹果')
print(fruits)

# del把变量完全删除
del fruits
print(fruits)






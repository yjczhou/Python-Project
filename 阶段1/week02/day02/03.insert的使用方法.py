# coding:utf-8

# 将一个元素添加到当前列表的指定位置
# list.insert(index,new_item) index:新元素放在哪个位置，new_item: 添加的新元素

# 如果insert 传入的位置 列表中不存在，则将新元素添加到列表结尾
# 字符串、元组、列表元素的位置是从0开始计算的
fruits = ['苹果', '西瓜', '水蜜桃']
fruits.insert(1,'柠檬')
print(fruits)

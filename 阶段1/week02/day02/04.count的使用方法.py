# coding:utf-8

# 列表（元组）的count函数
# 返回当前列表中某个成员的个数
# inttype = list.count(item) item: 你想查询的元素
# 如果查询的成员不存在，则返回0
# 列表只会检查 完整元素 是否存在 需要计算的内容
fruits = ['苹果', '西瓜', '水蜜桃','西瓜']
count = fruits.count('西瓜')
print(count)
count = fruits.count('西')
print(count)
print('-----------------------------------')
fruits = ('苹果', '西瓜', '水蜜桃','西瓜')
count = fruits.count('西瓜')
print(count)
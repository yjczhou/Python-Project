# coding:utf-8

# 以一定条件为基础的循环，条件满足则无限循环，条件不满足则退出循环
# 不依赖可迭代的数据类型，而for循环依赖
# while bool_result:
#   do
# bool_result: 布尔类型

count =1
while count<5:
    print(count)
    count += 1
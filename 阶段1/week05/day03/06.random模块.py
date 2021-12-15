# coding:utf-8

import random
'''random.random()'''
# 随机返回0-1之间的浮点数
print(random.random())


'''random.uniform(a,b)'''
# 产生一个a，b区间的随机浮点数
print(random.uniform(1,10))


'''random.randint(a,b)'''
# 产生一个a，b区间的随机整数
print(random.randint(1,10))


'''random.choice(obj)'''
# 返回对象中的一个随机元素
print(random.choice(['a','b','c']))
print(random.choice('abc'))
print(random.choice(('a','b','c')))

'''random.sample(obj,int)'''
# 随机返回对象中指定的元素
print(random.sample(['a','b','c'],2))
print(random.sample('abc',2))


'''random.randrange'''
# 获取区间内的一个随机数
# 1是步长
# 定义1 返回的就是0-99
# 定义2 返回的就是2 4 6 8 10...
print(random.randrange(0,100,1))
print(random.choice(range(0,100,1)))
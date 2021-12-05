# coding:utf-8

# []的获取方法
# 字典+中括号内穿key ，不进行赋值操作 即为获取
# 返回key对应的value
my_dict = {'name': 'dewei','age':'33'}
name = my_dict['name']
print(name)

# get()
# dict.get(key,default = None)
# key：需要获取value的key
# defalut：key不存在则返回默认值，默认是None，我们也可以自定义
age = my_dict.get('age')
print(age)

# 二者区别
# []如果获取的key不存在，则直接报错
# get如果获取的key不存在，则返回默认值
# 所以开发中，优先使用get函数
high = my_dict.get('high','175')
# high不存在，所以返回175
print(high)
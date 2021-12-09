# coding:utf-8

# for循环
# 通过for关键字将列表，元组，字符串，字典中每一个元素按照序列顺序进行遍历（循环
# for item in iterable:  # for循环语法
#   print(item)    # 每次循环对应的代码块，代码块需要缩进

# iterable ： 可循环的数据类型 如列表 元组 字符串 字典
# item ： iterable中的每一个元素

l = ['dewei','xiaomu','xiaoman','xiaoming']
for item in l:
    print(item)
print('-------------------------------------------------')   
for i in 'python':
    print(i)
print('-------------------------------------------------')
t = ('dewei','xiaomu','xiaoman','xiaoming')
for name in t:
    print(name)
print('-------------------------------------------------') 
users ={"name":'dewei','age':33}
for key in users:
    print(key)# 得到的是字典的key
    print(users[key])# 这样可以得到值
print('-------------------------------------------------') 
# 字典利用items内置函数进行for循环
# 将字典转成为列表，每个key，value转成元组
# for key,value in dict.items():
#   print(key,value)
# key: for循环体中获取的字典当前元素的key
# value：for循环体中对应当前key的值的value
# items()返回一个伪列表
d = {'name':'小慕','age':10}
d_items = d.items()
print(d_items)
# dict_items([('name', '小慕'), ('age', 10)])
for key,value in d.items():
    print(key,value)
# name 小慕
# age 10

user_list = [
    {'username':'xiaomu'},
    {'username':'dewei'}]
for user in user_list:
    print(user)
    print(user.get('username'))

print('-------------------------------------------------')
# python的内置函数--range
# 返回的是一个一定范围的可迭代对象，元素为整型，
# 他不是列表，无法打印信息，但可循环 
# for item in range(start,stop,step=1):
#     print(item)
# 注意range也算左含，右不含
# start : 开始的数字
# stop : 结束的数字
# step ： 跳步，类似索引中的第三个参数
# 返回一个可迭代（循环的）一整型为主的对象
l = range(5)
for item in l:
    print(item)

print('-------------------------------------------------')
# else在for循环中的使用
# else语句只有在for循环正常退出后执行
# 循环没有报错，中途没有停止
l = range(5)
for item in l:
    print(item)
else:
    print('for循环成功结束')
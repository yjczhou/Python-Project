# coding:utf-8

# len函数可以计算出除了 数字类型以外 ，其他所有数据类型的长度
names_list = ['xiaomu','dewei','xiaowang']
length = len(names_list)
print(length)

# 列表元素累加,累乘
new_names_list = names_list+names_list
print('累加',new_names_list)
new_names_list = names_list * 2
print('累乘',new_names_list)
names_list += ['lisi']
print('+=',names_list)
names_list *= 2
print('*=',names_list)
print('------------------------------------------------------------------')
# 元组
names_tuple = ('xiaomu','dewei','xiaowang')
length = len(names_tuple)
print(length)

new_names_tuple = names_tuple + names_tuple
print('累加',new_names_tuple)
new_names_tuple = names_tuple * 2
print('累乘',new_names_tuple)
names_tuple += ('lisi',)
print('+=',names_tuple)
names_tuple *= 2
print('*=',names_tuple)
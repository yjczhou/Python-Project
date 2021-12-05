# coding:utf-8

# copy()
# 功能
# 将当前列表复制一份相同的列表，新列表与就列表内容相同，但内存空间不同
# new_list = list.copy() 返回一个一模一样的列表
import copy

old_list = ['a','b','c']
new_list = old_list.copy()
print(new_list)
print('-------------------------------------------')
# copy与二次赋值的区别
a=[1,2,3]
b=a
a.append(4)
print(a)
print(b)
# 二次赋值的变量与原始变量享有相同的内存空间
# copy函数创建的新列表与原始列表不是一个内存空间，不同享数据变更
a = [1,2,3]
b= a.copy()
b.append(4)
print(b)
print(a)
print('-------------------------------------------')
# copy() 属于浅拷贝
'''
通俗的说，我们有一个列表a，列表里面的元素还是列表，当我们拷贝出新列表b
后，无论是a还是b的内部的列表中的数据发生了变化后，相互之间都会受到影响
---浅拷贝
'''
a = [[1,2,3],[4,5,6]]
b = a.copy()
print(b)
b[0].append(10)
# 此时b和a都会首影响
print(b)
print(a)
print('-------------------------------------------')
'''
深拷贝不仅对第一层数据进行了copy，对深层的数据也进行了copy，
原始变量和新变量完完全全并不共享数据
'''
a = [[1,2,3],[4,5,6]]
b = copy.deepcopy(a)
print(b)
b[0].append(10)
print(b)
print(a)

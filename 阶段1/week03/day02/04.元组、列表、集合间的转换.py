# coding:utf-8

# 列表元组集合间隔转换的函数
'''
原始类型        目标类型        函数      举例
列表           集合           set()     new_set = set([1,2,3,4,5])
列表           元组           tuple()   new_tuple = tuple([2,3,4,5])
元组           集合           set()     new_set = set((1,2,3,4,5))
元组           列表           list()    new_list = list((1,2,3,4,5))
集合           列表           list()    new_list = list({1,2,3,4,5})
集合           元组           tuple()   new_tuple = tuple({1,2,3,4,5})
'''
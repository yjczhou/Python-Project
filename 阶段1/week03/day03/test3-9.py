# coding:utf-8

n = 8

def new_dict(n):
    dict_new = {}
    for i in range(1,n+1):
        dict_new[i] = i*i
    print(dict_new)

new_dict(8)
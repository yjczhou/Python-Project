# coding:utf-8

'''lambda功能'''
# 定义一个轻量化的函数
# 即用即删除，很适合需要完成一项功能，但是此功能只在此一处使用

'''定义方法'''
# 冒号后面自带return效果
'''无参数'''
# f = lambda:value
# f()
'''有参数'''
# f=lambda x,y:x*y
# f(3,4)

f1 = lambda : 1
print(f1())
f2 = lambda x,y : x*y
print(f2(3,4))

users =[
    {'name':'dewei'},
    {'name':'xiaomu'},
    {'name':'asan'}
] 
# x指字典中的每一项
# 按照name排序
users.sort(key=lambda x:x['name'])
print(users)

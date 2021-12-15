# coding:utf-8

'''什么是迭代器'''
# 平时代码都是一次性加载到内存中

# 使用了迭代器后就可以按需加载到内存中
# 大大提升了效率

'''如何生成迭代器-iter'''
# 生成一个迭代器对象
# iter(iterable)
# iterable: 可迭代类型的数据类型。即可遍历的对象

# 例子
iter([1,2,3])
# <list_iterator at 0x5e3ce08>
# 返回一个迭代器对象

'''迭代器的使用-next'''
# 返回迭代器中的数据
# next(iterator)
# iterator: 迭代器对象

# 例子
# 每调用一次next(),才会把迭代器中的一个数据放在内存中
iter_obj = iter([1,2,3])

# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# # 超出的会报StopIteration
# print(next(iter_obj))

# 通过for循环得到迭代器的数据
for i in iter_obj:
    print(i)
print('-----------------------') 



'''迭代器常用方法之生成迭代器'''
# 1.for循环生成法--yield
#    yield把生成的每一个数据放入内存中

# 2.for循环一行生成迭代器


# 1.例子
def test():
    for i in range(10):
        # 把每次生成的i放入内存中
        yield i 
res = test()
# 只有调用next()函数的时候 for循环才会通过 yield把数据放入内存中
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
# ...

print('-----------------------') 
# 2.例子
res = (i for i in [1,2,3])
print(next(res))
print(next(res))
print(next(res))
print('-----------------------') 

'''迭代器常用方法之for循环获取'''
# 不会报错

# 例子
res = ( i for i in [1,2,3])

for item in res:
    print(item)
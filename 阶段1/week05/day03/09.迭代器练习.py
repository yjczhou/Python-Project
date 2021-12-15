# coding:utf-8

iter_obj = iter((1,2,3))

def _next(iter_obj):
    try:
        return next(iter_obj)
    except StopIteration:
        return None
    
# print(_next(iter_obj))
# print(_next(iter_obj))
# print(_next(iter_obj))
# print(_next(iter_obj))

# 通过iter生成的迭代器能否for循环
# for i in iter_obj:
#     print(i)

def make_iter():
    # 通过yield制作迭代器
    for i in range(10):
        yield i

iter_obj = make_iter()
print(type(iter_obj))
# <class 'generator'>
for i in iter_obj:
    print(i)

# 迭代器把数据放在内存中，每一次被读取后都会被释放
# 所以下面的迭代不会执行
print('-----------------------')
for i in iter_obj:
    print(i)

print('-----------------------')

iter_obj = (i for i in range(10))

for i in iter_obj:
    print(i)
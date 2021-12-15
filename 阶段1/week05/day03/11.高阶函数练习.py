# coding:utf-8

friuts = ['apple','banana','orange']

#result是一个可迭代的对象 
result = filter(lambda x: 'e' in x,friuts)
print(list(result))
# 上面使用过了，在内存中就会销毁，所以下面的不会执行
for i in result:
    print(i)

print('-----------------------')

def filter_func(item):
    if 'e' in item:
        return True

filter_result = filter(filter_func,friuts)

for i in filter_result:
    print(i)
    

map_result = map(filter_func,friuts)
print(list(map_result))
# [True, None, True]
# 由于第二个不含e

from functools import reduce
# 累加
add_result = reduce(lambda x,y:x+y,[0,1,2,3,4,5])
# 累乘
multip_result = reduce(lambda x,y:x*y,[1,2,3,4,5])
print(add_result) # 15
print(multip_result)

# 字符串累加
add_result_str = reduce(lambda x,y:x+y,friuts)
# 字符串累乘
multip_result_str = reduce(lambda x,y:x*y,friuts)
print(multip_result_str)
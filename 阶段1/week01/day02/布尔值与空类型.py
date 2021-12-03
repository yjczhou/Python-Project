# coding:utf-8

# bool型 bool()
'''
0     false   非0     true
0.0   false   非0.0   true
''    fasle   非空    true

'''

# 空类型
# 不属于任何类型就是空类型
# 固定值 None
# 空类型 属于false
# 不确定类型时，可以使用空类型
test = None
print(test)
# 知道类型就可以重新赋值
test = True
print(test)
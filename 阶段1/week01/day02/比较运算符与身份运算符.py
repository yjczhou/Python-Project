# coding:utf-8

'''
运算符        描述                             举例
 ==         判断是否等于                       a==b
 !=         是否不等于                         a!=b
 >          是否大于                           a>b
 <          是否小于                           a<b
 >=         是否大于等于                        a>=b
 <=         是否小于等于                        a<=b
 <>         是否不等于                         a<>b         仅在python2中可以使用
 is         判断两个对象存储单元是否相同           a is b
 is not     判断两个对象存储单元是否不相同          a is not b

 单元存储就是我们提过的内存块
'''

d = 18
d_01 = 18
f = 300
f_01 = 300
print(d==d_01)
print(d is d_01)
print('d id is:',id(d))
print('d_01 id is:',id(d_01))

print(f==f_01)
print(f is f_01)
print('f id is:',id(f))
print('f_01 id is:',id(f_01))


# 在原生的python解释器中，会实现定义0-255
# 所以两个变量相同并且在0-255内 is会是true

# 而在脚本中也行是因为我们在上面定义了300，后面变量也有相同的值，所以可以直接在已有的内存中拿过来用
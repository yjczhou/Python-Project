# coding:utf-8

'''必传参数'''
# 函数中定义的参数没有默认值，在调用函数时如果不传入则报错
# 在定义函数的时候，参数后边没有等号与默认值
# 在定义函数的时候，没有默认值且必须在函数执行的时候传递进去的参数，
# 且顺序与参数顺序相同，就是必传参数


'''默认参数'''
# 在定义函数的时候，定义的参数含有默认值，
# 通过赋值语句给他设一个默认的值
# def add(a,b=1)
# b就是默认参数
# 如果，哦热门参数在调用函数的时候给予了新的值，
# 函数将优先使用后传的值进行工作


'''不确定参数--可变参数'''
# 没有固定的参数名和数量(不知道要传参数的参数名具体是什么)
# def add(*args, **kwargs):
# add(1,2,3,name='dewei',age=33)
# 1,2,3对应*args ， 后面的对应**kwargs
# *args代表将未参数的值合并成元组
# **kwargs代表将有参数与默认值的复制语句合并成字典
def test(*args, **kwargs):
    print(args,type(args))
    print(kwargs,type(kwargs))

test(1,2,3,4,5,name='dewei',age=33,top=174)
print('--------------------------------------------------')
def test_supper(*args, **kwargs):
    if len(args)>=1:
        print(args[0])
    if 'name' in kwargs:
        print(kwargs['name'])
    else:
        print('no name')
    print('args:',args)
    print('kwargs:',kwargs)
test_supper(1,name='dewei')
print('--------------------------------------------------')
# 那如果我们直接传入元组和字典呢?
a=(1,2)
b={'name':'dewei','age':33}
test_supper(a,b)
print('--------------------------------------------------')
# 会转换成元组与字典，并不代表我们能直接传日元组与字典
# 但是我们可以这样写
test_supper(*a,**b)
print('--------------------------------------------------')

'''参数规则'''
# def add(a,b=1,*args, **kwargs):
# 参数的定义从左到右依次是：必传参数，默认参数，可变元组参数？，可变字典参数
# 函数的参数传递非常灵活
# 比串参数与默认参数的传参多样化

def test(a,b,*args):
    print(a,b,args)

s=(1,2)
test(1,2,*s)
# test(a=1,b=2,*s) 
#报错 ，采用赋值形传参的话，可变元组参数必须放在前面
# 下面这种方式不推荐
def test2(*args,a,b=1):
    print(a,b,args)
test2(*s,a=1,b=2)
test2(a=1,b=2,*s)
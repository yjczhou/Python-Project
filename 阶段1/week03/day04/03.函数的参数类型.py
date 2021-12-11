# coding:utf-8

# 参数定义类型的方法
# 参数名+冒号+类型函数
# 参数名+冒号+类型函数+等号+默认值
def person(name:str,age:int = 33):
    print(name,age)
# 韩式定义在python3.7之后可用

# 函数不会对参数类型进行验证,知识提示程序要是什么类型

def add(a:int,b:int=3):
    print(a+b)

add(1,2)
add('hello','xiaomu')# 不会报错
# helloxiaomu

def test(a:int,b:int=3,*arg:int,**kwargs:str):
    print(a,b,arg,kwargs)
    
test(1,2,3,'4',name='小慕')
# 1 2 (3, '4') {'name': '小慕'}

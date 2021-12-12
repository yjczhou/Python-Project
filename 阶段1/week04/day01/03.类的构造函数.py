# coding:utf-8

'''类的构造函数'''
# 类中一种默认函数，用来将类实例化的同时，将参数传入类中

'''构造函数的创建'''
# def __init__(self,a,b):
#     self.a = a
#     self.b = b

'''构造函数的用法'''

class Test(object):
    def __init__(self,a):
        self.a=a
    def  run(self):
        print(self.a)

# 1对应a
t=Test(1)
t.run()

class Person(object):
    def __init__(self,name,age=None):
        self.name = name
        self.age = age
    
    def run(self):
        print(f'{self.name}在奔跑')
    
    def jump(self):
        print(f'{self.name}在跳跃')
        
    def work(self):
        self.run();
        self.jump()

xiaomu = Person(name ='小慕',age=10)
# 可以使用调用属性的方法对参数进行修改
xiaomu.name = 'xiaomu'
xiaomu.work()
print('--------------------------------')
dewei = Person(name ='dewei',age=18)
dewei.work()


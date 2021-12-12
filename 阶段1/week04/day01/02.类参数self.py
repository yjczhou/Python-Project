# coding:utf-8

'''类参数self'''
# self是类函数中的必传参数，且必须放在第一个参数位置
# self 是一个对象，它代表实例化的变量自身
# self可以直接通过点来定义一个类变量 self.name = 'dewei'
# self中变量与含有self参数的函数可以在类中的任何一个函数内随意调用
# 非函数中定义的变量在定义的时候不用self

class Person(object):
    name = None
    age = None
    
    def run(self):
        print(f'{self.name}在奔跑')
    
    def jump(self):
        print(f'{self.name}在跳跃')
        
    def work(self):
        self.run();
        self.jump()
        # 在内部定义的函数可以不用加self
        def sleep(name):
            return name
        result = sleep(self.name)
        print('sleep result is',result)
xiaomu = Person()
xiaomu.name = '小慕'
xiaomu.jump()
print('---------------------')
xiaomu.work()
print('---------------------')
dewei = Person()
dewei.name = 'dewei'
dewei.jump()

# 实例化对象自定义属性
dewei.top = 174
print(dewei.top)
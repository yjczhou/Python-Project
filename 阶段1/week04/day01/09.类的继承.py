# coding:utf-8

'''类的继承'''
# 通过继承基类来得到基类的功能
# 所以我们把被继承的类称作父类或基类，继承者被称作子类
# 代码的重用

'''父类与子类的关系'''
# 子类拥有父类的所有属性和方法
# 父类不具备子类自有的属性和方法

# 例子
from os import name


class Person(object):
    def talk(self):
        print('talk')
    def think(self):
        print('think')

# 代表继承Person
# 定义子类时，将父类传入子类参数内
class Child(Person):
    def swimming(self):
        print('child can swimming')

# 子类实例化可以调用自己与父类的函数与变量
c = Child()
c.talk()
c.swimming()

p = Person()
p.talk()
# p.swimming()#报错，父类没有这个方法
print('-------------------------------------')

class Person_test(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    def talk(self):
        return f'{self.name} are talking'
    def is_sex(self):
        if self.sex == 'boy':
            return f'{self.name} is a boy'
        else:
             return f'{self.name} is a girl'

class ChildOne(Person_test):
    def play_football(self):
        return f'{self.name} are playing football'


class ChildTwo(Person_test):
    def play_pingpong(self):
        return f'{self.name} are playing pingpong'
c_one = ChildOne(name='小慕',sex='boy')
result = c_one.play_football()
print(result)
c_two = ChildTwo(name='小云',sex='girl')
result = c_two.play_pingpong()
print(result)
print(c_one.talk())
print(c_two.is_sex())

print('-------------------------------------')
p = Person_test(name='小慕爸爸',sex='boy')
print(p.talk())
print(p.is_sex())
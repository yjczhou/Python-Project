# coding:utf-8

'''什么是多重继承'''
# 可以继承多个基（父）类


'''多重继承方法'''
# 将被继承的类放入子类的参数为中，用逗号隔开
# 从左向有依次继承
# class Child(Parent1,Parent2,Parent3...)

# 1.书写两个基类
class Tool(object):
    def work(self):
        return 'tool work'
    def car(self):
        return 'car will run'

class Food(object):
    def work(self):
        return 'food work'
    
    def cake(self):
        return 'i like cake'

class Person(Tool,Food):
    # 占位符，避免因为不写类体而报错
    pass

if __name__ == '__main__':
    p = Person()
    p_car = p.car()
    print(p_car)
    p_cake = p.cake()
    print(p_cake)
    # 如果被继承的父类中有同名方法，优先继承第一个继承的父类里面的方法，即Tool
    p_work = p.work()
    print(p_work)
    
    # __mro__内置函数告诉我们一个类是如何继承的，以及继承顺序
    print(Person.__mro__)
 

        
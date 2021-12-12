# coding:utf-8

'''super函数作用'''
# 自累哦父类都有这个方法，但是我想在子类中使用父类的同名方法，就可以使用super
# python子类继承父类的方法而使用的关键字，当子类继承父类后，就可以使用父类的方法

'''super的用法'''

class Parent(object):
    def __init__(self,p):
        print('hello i am parent %s' % p)

class Child(Parent):
    def __init__(self,c,p):
        print('hello i am child %s' % c)
        # 在python3.0之后的时代super里面的参数不用传也可以
        # 代表我们想执行Parent的构造方法__init__
        # p是传参给父类
        # 也可以在这里直接传，不用实例化的方式
        # 'parent'
        super(Child,self).__init__(p)
        #   当前类 类的实例 使用父类的方法

if __name__ == '__main__':
    # c = Child()
    # hello i am child
    # hello i am parent 
     c = Child(c='child',p='parend')
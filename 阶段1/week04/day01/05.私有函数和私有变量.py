# coding:utf-8

'''私有函数和私有变量'''
# 无法被实例化后的对象调用的类中的函数与变量
# 类的内部可以调用私有函数与变量
# 只希望类内部调用使用，不希望被使用者调用

'''私有函数和私有变量的定义方法'''
# 在变量或函数前添加__（两个下划线），变量或函数名后面无序添加
# 例子：
# class Person(object):
#     def __init__(self,name):
#         self.name = name
#         # 私有变量
#         self.__age = 33
#     def dump(self):
#         print(self.name,self.__age)
#     # 私有函数
#     def __cry(self):
#         return 'I am cry'

class Cat(object):
    __cat_type = 'cat'
    def __init__(self, name,sex):
        self.name = name
        self.__sex = sex
        
    def run(self):
        # pass内置函数，相当于一各占位符
        # 如果我们只定义一个函数名，不写函数体就会报错
        # 所以我们可以使用占位符
        # pass
        result = self.__run()
        print(result)
    
    def __run(self):
        return f'{self.__cat_type},小猫{self.name}{self.__sex}开心的奔跑者'

    def dump(self):
        # pass
        result = self.__dump()
        print(result)
    
    def __dump(self):
        return f'{self.__cat_type},小猫{self.name}{self.__sex}开心的跳跃者'
cat = Cat(name='xiaomi',sex='boy')
cat.run()
cat.dump()
print('--------------------------------')
# 报错
# 私有函数无法通过实例化对象调用
# cat.__run()
# cat.__dump()

# 但是我就是要调用要怎么办呢？
# print(dir(cat))
# ['_Cat__dump', '_Cat__run', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
#  '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#  '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
#  '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'dump', 'name', 'run']
print(cat._Cat__dump())
print(cat._Cat__run())

        
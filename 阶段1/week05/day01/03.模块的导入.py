# coding:utf-8

'''模块的导入from .. import .. '''

# 通过从某个包中找到对应的模块
# from package import module
# package: 来源包名
# module：包中的目标模块

# 例子
# from animal import dog
# dog.run()
# 我们通过from import 直接找到了dog模块，所以只需要使用dog模块直接用.的方式找到里面的方法并
from animal.dog import action
print(action.run())
# 可以给action起别名
from animal.dog import action as dog
print(dog.run())

# 直接导入方法
from animal.cat.action import run
print(run())

# 
from animal import main
print(main.animal())
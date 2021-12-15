# coding:utf-8

# 可以在这个文件里导入animal里面包的模块
# 在别的文件中写就不需要写哪么长，直接from animal import cat_action     cat_action.run()
# 如test1.py中
from .cat import action as cat_action
from .dog import action as dog_action

# def animal_test():
#     return 'animal_test'
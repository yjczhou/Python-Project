# coding:utf-8

'''全局变量'''
# 在python脚本最上层代码块的变量
# 全局变量可以在函数内被读取使用

name = 'dewei'

def test():
    print(name)
test()

def test1():
    # 这里的name是局部变量
    # 函数内部只能读取全局变量，但是不能修改全局变量
    name = 'xiaomu'
    print('函数内部',name,id(name))
test1()
print('全局变量',name,id(name))

# global关键字
# 将全局变量可以在函数体楼内进行修改
# 工作中不建议使用global对全局变量进行修改
# global 只支持数字，字符串，空类型，布尔值
def test2():
    # global + 全局变量名
    global name
     # 函数体内给全局变量重新赋值xiaomu
    name = 'xiaomu'
    print('global',name,id(name))
test2()
print('全局的',name,id(name))




# 在局部使用字典，列表类型是不需要global的
test_dict = {'a':1,'b':2}
def test3():

    test_dict['c']=3
test3()
print(test_dict)
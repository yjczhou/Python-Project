# coding:utf-8

'''
常用函数
函数名      参数        介绍                        返回值          举例
abs         Number      返回数字的绝对值            正数字          abs(-10)
all         List        判断列表内容是否全是true     Bool           all(['','123'])
help        object      打印对象的用法              无              help(list)
enumerate   iterable    迭代时记录索引              无              for index,item in enumerate(list)
input       Str         命令行输出如消息            Str             input('请输出信息')
'''

print(abs(-10))
# None判定bool值的时候为False
print(all(['a' in 'abc',True,None]))
print(all(['a' in 'abc',True,len('abc')]))

# 枚举函数
python =['django','flask','tornado']

for index,item in enumerate(python):
    print(index,item)
    

# food = input('你想吃些什么?')
# print(food)

# 帮助文档
help(input)


'''
常用函数
函数名      参数        介绍                            返回值          举例
isinstance  Obj,type    判断对象是否是某种类型          bool            isinstance('a',str)
type        Obj         判断对象的类型                  str            type(10)
vars        instance    返回实例化的字典信息            dict            
dir         Obj         返回对象中的所有可用方法和属性  list            dir('asd')
hasattr     Obj,key     判断对象中是否有某个属性        bool            hasattr('1','upper')

setattr     obj,key,val 为实例化对象添加属性与值        无              setattr(instance,'run','go')
getattr     obj,key     通过队形获取属性                任何类型        getattr(obj,key)
any         iterable    判断内容是否有true              bool           any([1,0,' '])
'''

class Test(object):
    a=1
    b=2
    def __init__(self):
        self.a = self.a
        self.b = self.b

test = Test()
result = vars(test)
print(result)

# True
print(hasattr(test,'a'))
# False
print(hasattr(test,'c'))

setattr(test,'c',3)
print(test.c)

if hasattr(list,'append'):
    print(getattr(list,'append'))
else:
    print('不存在')
    
    
a = ['',None,True,0]
print(any(a))
# True
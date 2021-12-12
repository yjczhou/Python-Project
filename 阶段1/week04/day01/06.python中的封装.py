# coding:utf-8

'''封装的概念'''
# 将不对外的私有属性或方法通过可对外使用的函数而使用（类中定义私有的，只有类内部使用，外部无法访问）
# 保护隐私，明确区分内外

# 例子：
class Parent(object):
    def __hello(self,data):
        print('hello %s'% data )
        
    def helloword(self):
        self.__hello('world')

if __name__ == '__main__':
    p = Parent()
    p.helloword()
# coding:utf-8

class Base_study(object): 
    def study(self):
        print( "通过阅览书籍丰富知识") 
        
class Man_study(Base_study):
    def study(self): 
        super(Man_study,self).study() 
        print("通过报刊丰富知识")
        
class Woman_study(Base_study):
    def study(self): 
        super(Woman_study,self).study()
        print("通过阅览新闻丰富知识") 
        
man=Man_study() 
woman=Woman_study()
woman.study()
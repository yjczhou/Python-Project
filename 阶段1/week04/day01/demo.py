# coding:utf-8

def log(func): 
    def wrapper(): 
        print('call %s():' % func.__name__) 
        func() 
    return wrapper

@log 
def hello():
    print("hello world")

def now():
    print('2018-11-27')
    
now()
hello()
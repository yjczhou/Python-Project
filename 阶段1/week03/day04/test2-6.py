# coding:utf-8

def seq(num,num1,num2):
    if num < 88:
        print(num1*num2)
    else:
        print(num1+num2)

tuple = (5,2,1)
seq(*tuple)
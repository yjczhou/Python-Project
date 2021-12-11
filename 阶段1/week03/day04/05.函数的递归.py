# coding:utf-8

# 一个函数不停的将自己反复执行
# 递归函数的定义方法
# def test(a):
#     print(a)
#     return test(a)

# 递归函数的说明
# 内存溢出
# 避免滥用递归

# 打印指定位置的斐波那锲数列
def f(i):
    if i == 1 or i == 2:
        return 1
    else:
        return f(i-1)+f(i-2)
result = f(5)
print(result) 

# 打印指定范围内的斐波那锲数列
def num(start,end):
    for i in range(start,end+1):
        print(f(i),' ',end='')
num(1,10)
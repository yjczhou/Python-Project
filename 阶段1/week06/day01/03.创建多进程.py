# coding:utf-8

'''进程的创建'''

'''进程的创建模块--multiprocessing
函数名      介绍            参数                返回值
Process     创建一个进程    target,args         进程对象

start       执行进程        无                  无
join        阻塞程序        无                  无
kill        杀死进程        无                  无
is_alive    进程是否存活    无                  bool
'''

'''多进程的问题'''
# 通过进程模块执行的函数无法获取返回值
# 多个进程同时修改文件肯会出现错误
# 进程数量太多会造成资源不足，甚至死机等情况



import time
import os
# 导入多进程模块
import multiprocessing

def work_a():
    for i in range(10):
        # os.getpid() 返回当前函数执行到的位置，进程号码
        print(i,'a',os.getpid())
        time.sleep(1)


def work_b():
    for i in range(10):
        print(i,'b', os.getpid())
        time.sleep(1)

if __name__ == '__main__':
    start = time.time() # *主进程
    # 情况1.
    # 是同一个进程id
    # 说明在同一个进程在执行
    # work_a() # *主进程
    # work_b() # *主进程
    
    # 情况2.
    # 创建work_a函数另一个进程
    a_p = multiprocessing.Process(target=work_a)
    # 在python终端中运行才有a进程的效果
    # 两者进程号是不一样的
    # 除了a_p都是主进程上的程序
    # a_p是在主进程中创建的子进程
     # 开始执行这个进程
    # a_p.start()
    # work_b() # *主进程
    
    # 情况3.
    # 创建名为work_b的子进程
    b_p = multiprocessing.Process(target=work_b)
    # 执行两个子进程
    # a_p.start()
    # b_p.start()
    # ? 方法技巧：平时一把会创建多个进程，手动start()麻烦,可以利用for循环
    # for p in (a_p,b_p):
    #     p.start()    
    # # 一般都是主进程先执行的，但我们可以阻塞
    # for p in (a_p,b_p):
    #     p.join()
    # # 直到阻塞的进程执行完才会执行下面的程序
    # for p in (a_p,b_p):
    #     print(p.is_alive())
    
    # 情况4.
    a_p.start()
    # 先把a_p子进程执行完
    a_p.join()
    b_p.start()
    
    # 主进程会先执行
    # 计算程序运行时间
    print(time.time() - start) # *主进程
    # 父进程id
    print('父进程pid是%s' % os.getpid()) # *主进程
    
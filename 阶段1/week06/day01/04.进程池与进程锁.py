# coding:utf-8

'''什么是进程池'''
# 一个进程池里包含许多进程
# 进程池中的进程不会被关闭，可以反复被使用
# 避免了创建与关闭的消耗

'''进程池的创建-multiprocessing
函数名          介绍                    参数                        返回值
Pool            进程池创建              Processcount(进程数)        进程池对象

apply_async     任务加入进程池（异步）   func，args                  无
close           关闭进程池              无                          无
join            关闭进程池任务结束      无                          无
'''

'''进程锁'''
'''进程锁的枷锁与解锁'''
# from multiprocessing import Manager
# manager = Manager()
# lock = manager.Lock()
'''
函数名          介绍            参数            返回值
acquire         上锁            无              无
release         开锁(解锁)      无              无
'''




import os
import time
import multiprocessing
from multiprocessing import Manager

def work(count,lock):
    # 进程加锁
    # 进程加锁后每次只执行一个进程
    lock.acquire()
    
    print(count,os.getpid())
    time.sleep(5)
    
    # 进程解锁
    lock.release()
    # 通过进程模块执行的函数无法获取返回值
    # 但是我们可以通过异步函数apply_async获得
    return 'result is %s,pid is %s' % (count, os.getpid())
    

if __name__ == '__main__':
    # 创建进程池,里面有5个进程
    pool = multiprocessing.Pool(5)
    # 实例化进程锁
    manager = multiprocessing.Manager()
    lock = manager.Lock()
    
    results = []
    for i in range(20):
        # 当进程池空闲的时候，才会把下一批任务放入进程池中
        # 可以通过异步函数得到返回值
        
        # 加了进程锁后每次只执行一个进程
       result =  pool.apply_async(func=work,args = (i,lock))
    #    results.append(result)
    
    # 并且通过这种方式也不需要下面的关闭阻塞代码
    # for res in results:
    #     #get函数获取异步函数的返回值
    #     # print(res)
    #     print(res.get())
    
    # 进程池是主进程的一部分，如果主进程已经结束了，进程池就不会执行，所以下面要加一行代码
    # time.sleep(20)
    
    # 当然也可以这么解决
    # 关闭进程池
    pool.close()
    # 等进程池结束了，才会执行下面的代码
    pool.join()
# coding:utf-8

'''线程池-concurrent
方法名                              说明                            举例
futures.ThreadPoolExcutor           创建线程池                      tpool = ThreadPoolExecutor(max_workers)
'''

'''
方法名          说明                            用法
submit          往线程池中加入任务              submit(target,args)
done            线程池中某个线程是否完成了任务   done()
result          获取当前线程执行任务的结果       result()
'''

import os
import time
# 导入线程模块
import threading
# 导入线程池模块
from concurrent.futures import ThreadPoolExecutor

# 设置线程锁
lock = threading.Lock()

# 线程不用把锁传入函数中，而进程需要
def work(i):
    # 线程所上锁
    # lock.acquire()
    print(i,os.getpid())
    time.sleep(1)
    # 线程锁开锁
    # lock.release()
    return 'result %s' % i
    
if __name__ == '__main__':
    # 打印主进程的id
    print(os.getpid())
    
    results =[]
    # 实例化线程池
    # 最大允许两个线程
    t = ThreadPoolExecutor(2)
    for i in range(20):
        t_result = t.submit(work,i)
        results.append(t_result)
    for res in results:
        print(res.result())


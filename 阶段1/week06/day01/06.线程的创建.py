# coding:utf-8

'''线程的创建-threading
方法名      说明            举例
Thread      创建线程        Thread(target,args)
'''

'''线程对象的方法
方法名          说明                用法
start           启动线程            start()
join            阻塞知道线程结束    join(timeout=None)
getName         获取线程的名字      getName()
setName         设置线程的名字      setName(name)
is_alive        判断线程是否存活    is_alive()
setDaemon       守护线程            setDaemon(True)
'''
'''线程的问题'''
# 通过线程执行的函数无法获取返回值
# 多个线程同时修改文件可能造成数据错乱





import time
import  random
# 导入多线程模块
import threading

lists = ['python','django','tornado','flask','bs5','uvloop']

new_list = []

def work():
    if len(lists) ==0:
        return
    data = random.choice(lists)
    lists.remove(data)
    new_data = '%s_new' % data
    new_list.append(new_data)
    time.sleep(1)

if __name__ == '__main__':
    start = time.time()
    # 普通方式
    # for i in range(len(lists)):
    #     work()
    
    # 线程的方式
    t_list = []
    for i in range(len(lists)):
        # 创建work函数子线程
        t = threading.Thread(target = work)
        # 把每一个线程对象传递进t_list数组
        t_list.append(t)
        # 启动每一个子线程
        t.start()
    # 为了将每一个线程对象阻塞
    for t in t_list:
        t.join()
    
    print('old_list:',lists)
    print('new_list:',new_list)
    print('time is %s' % (time.time()- start))
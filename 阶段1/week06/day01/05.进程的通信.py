# coding:utf-8

'''进程之间的通信'''
# 需要队列来实现

'''队列的创建-multiprocessing
函数名      介绍            参数                                 返回值
Queue       队列的创建      mac_count(最大传递多少信息)           队列对象

put         信息放入队列    message                              无
get         获取队列信息    无                                   str 
'''

import json
import time
import multiprocessing

class Work(object):
    # q是传入的队列对象
    def __init__(self,q):
        self.q = q
    
    # 发送信息
    def send(self,message):
        if not isinstance(message,str):
            # 序列化
            message = json.dumps(message)
        self.q.put(message)
    
    # 批量发送数据
    def send_all(self):
        for i in range(20):
            self.q.put(i)
            time.sleep(1)
    # 接受消息
    def receive(self):
        # 接受消息是源源不断的接收
        while True:
            result = self.q.get()
            try:
                # 反序列化
                res = json.loads(result)
            except:
                res = result
            print('recv is %s' % res)
            
if __name__ == '__main__':
    q = multiprocessing.Queue()
    # 实例化work类
    work = Work(q)
    # 创建一个发送消息的子进程
    send = multiprocessing.Process(target=work.send,args=({'name':'xiaomu'},))
    
    # 创建一个接受消息的子进程
    recv = multiprocessing.Process(target=work.receive)
    
    # 创建一个不断发送消息的进程
    send_all_p = multiprocessing.Process(target=work.send_all)
    
    
    # 执行子进程
    send.start()
    send_all_p.start()
    recv.start()
    
    
    # time.sleep(2)
    send_all_p.join()
    
    
    # 由于接受进程不知道上面时候是结束，所以我们要手动关闭接受进程
    recv.terminate()
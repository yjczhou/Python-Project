# coding:utf-8

import os
import time
import random
import gevent



def gevent_a():
    for i in range(10):
        print(i,'a gevent',os.getpid())
        # 这里不能使用time级别的sleep，因为这是cpu级别的
        # 我们应该使用asyncio里面的sleep
        gevent.sleep(random.random() * 2)
    return 'a gevent function'

def gevent_b():
    for i in range(10):
        print(i,'b gevent',os.getpid())
        # 这里不能使用time级别的sleep，因为这是cpu级别的
        # 我们应该使用asyncio里面的sleep
        gevent.sleep(random.random() * 2)
    return 'b gevent function'

# async def main():
#     result = await asyncio.gather(
#         a(), b()
#     )
#     print(result)
    
if __name__ == '__main__':
    start = time.time()
    # a()
    # b()
    g_a = gevent.spawn(gevent_a)
    g_b = gevent.spawn(gevent_b)
    gevent_list = [g_a,g_b]
    result = gevent.joinall(gevent_list)
    print(result[0].value)
    print(result[1].value)
    print(time.time() - start)
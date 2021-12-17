# coding:utf-8

import os
import time
import random
import asyncio



async def a():
    for i in range(10):
        print(i,'a',os.getpid())
        # 这里不能使用time级别的sleep，因为这是cpu级别的
        # 我们应该使用asyncio里面的sleep
        await asyncio.sleep(random.random() * 2)
    return 'a function'

async def b():
    for i in range(10):
        print(i,'b',os.getpid())
        # 这里不能使用time级别的sleep，因为这是cpu级别的
        # 我们应该使用asyncio里面的sleep
        await asyncio.sleep(random.random() * 2)
    return 'b function'

async def main():
    result = await asyncio.gather(
        a(), b()
    )
    print(result)
    
if __name__ == '__main__':
    start = time.time()
    # a()
    # b()
    
    asyncio.run(main())
    print(time.time() - start)
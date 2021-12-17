# coding:utf-8

'''异步'''
# 轻量级的线程  也叫协程
# 可以获取异步函数的返回值
# 主进程需要异步才行
# 更适合文件读写使用

'''async与await关键字'''
# async代表定义异步
# async def test():
#     return 'a'
# await 执行异步
# async def handle():
#     result = await test()


'''async调用async函数
函数名          介绍                参数                返回值
gather          将异步函数批量执行  asyncfunc           List 函数的返回结果
run             执行主异步函数      [task]              执行函数的返回结果
'''
# import asyncio
# async def main():
#     result = await asyncio.gather(
#         a(),
#         b()
#     )
#     print(result)

# if __name__ == '__main__':
#     asyncio.run(main())

'''gevent'''
# pip install gevent
# Microsoft Visual C++
# pip install wheel

'''gevent模块常用方法
函数名          介绍                    参数                    返回值
spawn           创建协程对象            Func，args              协程对象
joinall         批量处理协程对象        [spawnobj]              [spawnobj]
'''
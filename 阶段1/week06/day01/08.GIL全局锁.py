# coding:utf-8


'''GIL的作用'''
# 单一cpu工作
# 线程安全
# 只有默认的python解释器才会有GIL去全局锁
# 可以使用pypy的解释器执行代码，不会用GIL全局锁
# 或者使用 多进程+多线程
# coding:utf-8

'''日志的作用'''
# 日记
# 程序行为
# 重要信息记录

'''日志等级'''
# debug
# info
# warnning
# error
# critical

'''logging模块的使用'''
# logging.basicConfig
'''
参数名      作用            举例
level       日志等级        level = logging.DEBUG   由于debug级别最低，所以这样设置，所有信息都会被记录
format      日志输出格式    
filename    存储位置        filename = 'd://back.log'
filemode    输入模式        filemode = 'w'
'''

'''format具体格式
格式符          含义
%(levelname)s   日志级别名称
%(pathname)s    执行程序的路径
%(filename)s    执行程序名
%(lineno)d      日志的当前行号
%(asctime)s     打印日志的时间
%(message)s     日志信息
'''
# 常用模板
# format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'

import logging
import os

# logging.basicConfig(level=logging.DEBUG,
                    # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
# logging.info('你好 xiaomu')
# 2021-12-14 21:29:58,533 <ipython-input-3-3a1a4674eb1c>[line:1] INFO 你好 xiaomu
# logging.error('你好 xiaomu')
# 2021-12-14 21:32:31,549 <ipython-input-2-0822e6a959b9>[line:42] ERROR 你好 xiaomu

# 这样可以解决日志中文乱码问题
# file = open('back.log','w',encoding='utf-8')
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     # filename='back.log',
#                     stream=file)
# logging.info('这是第一个记录的日志信息')
# logging.warning('这是一个警告')
# logging.error('这是一个重大的错误信息')
# file.close()

# 优化
def init_log(path):
    if os.path.exists(path):
        # 存在就追加
        mode = 'a'
    else:
        # 不存在就创建
        mode = 'w'
    file = open(path,mode,encoding='utf-8')
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    # filename='back.log',
                    stream=file)
    return logging,file

current_path = os.getcwd()
path = os.path.join(current_path,'new_back.log')

log,file = init_log(path)
log.info('这是第一个记录的日志信息')
log.warning('这是一个警告')
log.error('这是一个重大的错误信息')
file.close()
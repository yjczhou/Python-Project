# coding:utf-8

'''sys中常用方法'''
'''
函数名              参数    介绍                    举例                        返回值
modules             无      py启动时加载的模块      sys.modules                 列表
path                无      返回当前py的环境路径    sys.path                    列表
exit                arg     退出程序               sys.exit()                  无
getdefaultencoding  无      获取系统编码            sys.getdefaultencodind()    字符串

platform            无      获取当前系统平台        sys.platform              字符串
version(属性)       无      获取python的版本        sys.version                 字符串
argv                *arg    程序外部获取的参数      sys.argv                    列表

'''

import sys
from types import CodeType
command = sys.argv[1]
if command == 'modules':
    modules = sys.modules
    print(modules)
elif command == 'path':
    print('-------------------------------------------------------------------------------------')
# sys.exit(1)
    path = sys.path
    print(path)
elif command == 'encoding':
    code = sys.getdefaultencoding()
    print(code)
    print('-------------------------------------------------------------------------------------')
elif command == 'platform':
    print(sys.platform)
    print('-------------------------------------------------------------------------------------')
elif command == 'version':
    print(sys.version)
    print('-------------------------------------------------------------------------------------')
else:
    print('not command')

# 这样使用
#  python .\09.python中的sys模块.py version
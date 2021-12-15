# coding:utf-8

'''os的文件域目录函数介绍'''
# import os
'''
函数名      参数        介绍                举例                                    返回值
getcwd      无          返回当前的路径      os.getcwd()                             字符串
listdir     path        返回指定路径下所有  os.listdir('c://Windows')               返回一个列表
                        的文件或文件夹      
makedirs    path mode   创建多级文件夹      os.makedirs('d://imooc/py')             无
removedirs  path        删除多级文件夹      os.removedirs('d://imooc','d://imoc')   无
rename      oldname     给文件或问价夹改名  os.rename('d://imooc','d://imoc')       无
            newname
rmdir       path        只能删除空文件夹    os.rmdir('d://imooc')                   无
'''

import os
# 获得当前路径
current_path = os.getcwd()
print(current_path)

new_path = '%s/test1/abc' % current_path
# 创建文件夹
# os.makedirs(new_path)

# 列出当前路径里的文件
data = os.listdir(current_path)
print(data) 

# 删除文件夹
# os.removedirs('test1/abc')

# 修改文件夹名字
# os.rename('test1','test_new')
# 修改文件名字
# os.rename('test_new/wenjian.txt','test_new/文件.txt')

# 删除空文件夹
os.rmdir('test_new/abc')
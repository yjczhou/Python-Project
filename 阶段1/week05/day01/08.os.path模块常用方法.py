# coding:utf-8

'''os.path模块常用方法'''
'''
函数名      参数         介绍               举例                        返回值
exists      path        文件或路径是否存在  os.path.exists('d://')      bool
isdir       path        是否是路径         os.path.isdir('d://')        bool
isabs       path        是否是绝对路径      os.path.isabs('test')       bool
isflie      path        是否是文件          os.path.isfile('d://a.py')  bool
join        path,path*  路径字符串合并      os.path.join('d://','test') 字符串
split       path        以最后一层路径      os.path.split('d://test')   列表
                        为基准切割      
'''

import os
# 获得当前路径
current_path = os.getcwd()
print(current_path)
print(os.path.isabs(current_path))
print(os.path.isabs('animal'))

new_path = '%s/test1' % current_path
# 创建文件夹
if not os.path.exists(new_path):
    os.makedirs(new_path)

new_path2 = os.path.join(current_path,'test2','abc')
if not os.path.exists(new_path2):
    os.makedirs(new_path2)

if not os.path.exists('test3'):
    os.makedirs('test3')
    
# if os.path.exists('test2/abc'):
#     os.removedirs('test2/abc')
    
# if os.path.exists('test3'):
#     os.rename('test3','test3_new')

# if os.path.exists('%s/test3_new' % current_path):
#     os.rmdir('%s/test3_new' % current_path)

# 使用场景，将一个带有文件的路径，进行左右分割
print(os.path.split(current_path))
# ('d:\\python项目\\阶段1\\week05', 'day01')
# coding:utf-8

'''文件操作的模式之读取
模式        介绍
r           读取文件
rb          二进制形式读取文件
'''

'''文件对象化的操作方法之读
方法名      参数        介绍                    举例
read        无          返回整个文件字符串      f.read()
readlines   无          返回文件列表           f.readlines()
readline    无          返回文件中的一行        f.readline()
mode        无          文件模式                f.mode
name        无          返回文件名称            f.name
closed      无          文件是否关闭            f.closed
'''

f = open('b.txt','r',encoding='utf-8')
# 返回整个文档,字符串类型
# data = f.read()

# 返回一个列表
# data = f.readlines()
# ['python很有意思python很有意思今天天气很好很适合学习pythonpython是非常简单的编程语言python很有意思\n',
# '今天天气很好\n', '很适合学习python\n', 
# 'python是非常简单的编程语言\n']

# _data = []
# for item in data:
#     temp = item.strip()
#     if temp != '':
#         _data.append(temp)

# ['python很有意思python很有意思今天天气很好很适合学习pythonpython是非常简单的编程语言python很有意思', 
# '今天天气很好', '很适合学习python',
# 'python是非常简单的编程语言']

# 返回一行数据
data = f.readline()
print('打开文件的模式',f.mode)
print('文件的名字',f.name)
print('文件是否已经关闭',f.closed)
f.close()
print('文件是否已经关闭',f.closed)
print(data)
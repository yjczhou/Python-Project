# coding:utf-8

'''正则表达式中的符号
符号        描述
re1|re2     匹配正则表达式re1或re2
^           匹配字符串起始部分
$           匹配字符串终止部分
*           匹配0次或者多次前面出现的正则表达式
+           匹配1次或者多次前面出现的正则表达式

{N}         匹配N次前面出现的正则表达式
{M,N}       匹配M-N次前面出现的正则表达式
[...]       匹配来自字符集的任意单一字符
[..x-y..]   匹配x-y范围中的任意单一字符
[^...]      不匹配次字符集中出现的任何一个字符，包括某一范围的字符（如果在此字符中出现）
\           将特殊字符无效化
'''

import re

data = 'dewei@imooc.com'

#  |或的关系，只要存在就能捕获
# 匹配道德数据只按字符串顺序返回，而不是按照匹配规则返回
print(re.findall('dewei|com|imooc',data))
# ['dewei', 'imooc', 'com']

# ? '^'等同于\A
print(re.findall('^dewei',data))# ['dewei']

print(re.findall('^haha',data))# []

# ? '$'等同于\Z
print(re.findall('com$',data))# ['com']

print(re.findall('mnet$',data))# []

# ? \w匹配字母数字下划线
# ? '*'可以匹配0次或多次
# @ . 都不满足\w，但是可以匹配0次，所以有空格匹配出来
print(re.findall('\w*',data))# ['dewei', '', 'imooc', '', 'com', '']
# ? '+'可以匹配1次或多次
print(re.findall('\w+',data))# ['dewei', 'imooc', 'com']

# ? \w等同于[a-zA-Z0-9_]
print(re.findall('\w{3}',data))# ['dew', 'imo', 'com']
# 匹配小写字母3次
print(re.findall('[a-z]{3}',data))# ['dew', 'imo', 'com']
#  匹配1到5次
print(re.findall('\w{1,5}',data))# ['dewei', 'imooc', 'com']

# 不匹配dewei中任何一个字符
print(re.findall('[^dewei]',data))
# ['@', 'm', 'o', 'o', 'c', '.', 'c', 'o', 'm']


'''组的概念
符号    描述
()      在匹配规则中获取指定的数据
'''

test = 'hello my name is dewei'
result = re.search('hello (.*) name is (.*)',test)
print(result.groups())
# ('my', 'dewei')
print(result.group(1))
# my
print(result.group(2))
# dewei


'''贪婪与非贪婪'''
# 0次或多次属于贪婪模式
# 通过?组合变成非贪婪模式
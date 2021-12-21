# coding:utf-8

'''正则表达式中的特殊字符
特殊字符    描述
\d          匹配任意十进制数字，与[0.9]一致
\D          匹配任意非数字
\w          匹配任何字母数字下滑线字符
\W          匹配非字母数字及下划线
\s          匹配任何空格字符，与[\n\t\r\v\f]
\S          匹配任意非空字符

\A          匹配字符串的起始
\Z          匹配字符串的结束
.           匹配任何字符(除了\n之外)
'''


'''正则表达式的使用'''
import re

data = 'hello dewei you are 33 age old'
# findall()匹配所有
# ? 匹配任意十进制数字，与[0.9]一致
print(re.findall('\d',data)) #['3', '3']
# ? 匹配任何空格字符，与[\n\t\r\v\f]
print(re.findall('\s',data)) #[' ', ' ', ' ', ' ', ' ', ' ']

data = 'i am dewei, i am 33'
# ? 匹配任何字母数字下滑线字符
print(re.findall('\w',data)) 
#['i', 'a', 'm', 'd', 'e', 'w', 'e', 'i', 'i', 'a', 'm', '3', '3']

data = 'hello dewei you are 33 age old'
# ? 匹配开头
print(re.findall('\Ahello',data))# ['hello']
print(re.findall('\Aheools',data))# []

# ? 匹配结尾
print(re.findall('old\Z',data))# ['old']
print(re.findall('aold\Z',data))# []

# ? 匹配任何字符
data = 'i am dewei'
print(re.findall('.',data))
# ['i', ' ', 'a', 'm', ' ', 'd', 'e', 'w', 'e', 'i']
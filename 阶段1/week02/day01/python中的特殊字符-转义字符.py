# coding:utf-8

# 转义字符
# 字符要转成其他含义的功能，所以我们叫他转义字符
# \+字符
'''
符号          说明
\n          换行，一般用于末尾，strip对其也有效
\t          横向制表符
\v          纵向制表符（会有一个男性符号）
\a          哑铃
\b          退格符，将光标迁移，覆盖（删除前一个）
\r          回车
\f          翻页(会出现一个女性符号)
\'          转义字符串中的单引号
\"          转义字符串中的双引号
\\          转义斜杠
'''
info_n = 'my name \n is dewei'
info_t1 = 'my name \t is dewei'
info_t2 = 'my name\tis dewei'
info_v = 'my name \vis dewei'
info_a = 'my name \ais dewei'
info_b = 'my name is dewei\b'
info_r = 'my name \ris dewei' #会把前面的字符删掉然后换行
info_f = 'my name \fis dewei'
print(info_n)
print(info_t1)
print(info_t2)
print(info_v)
print(info_a)
print(info_b)
print(info_r)
print(info_f)
print('my name is \'dewei\'')
print('my name is \"dewei\"')
print('my name is \\dewei\\')

# 转义无效符
# 在python中在字符串前面加r来将当前字符串的  转义字符无效化
print('hello \n nihao')
print(r'hello \n nihao')

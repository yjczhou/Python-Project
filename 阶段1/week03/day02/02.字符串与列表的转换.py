# coding:utf-8

'''字符串转列表的函数--split'''
# 将字符串以一定规则切割转成列表
# list = string.split(sep =None,maxsplit = -1)
# sep: 切割的规则分隔符，不填写，默认空格，如字符串无空格则不分割生成列表
# maxsplit: 根据切割符切割的次数，默认-1无限制
# 返回一个列表
info ='my name is dewei'
info_list = info.split()
print(info_list)

a='abc'
print(a.split())
b='a,b,c'
print(b.split(','))
c='a|b|c|d'
print(c.split('|',1))
'''列表转字符串的函数--join'''
# 将列表以一定的规则转成字符串
# str = 'sep'.join(iterable)
# sep:生成字符串用来分割列表每个元素的符号
# iterable:非数字类型的列表或元组或集合
# 返回一个字符串

# 列表中只能是字符串形式的才能拼接
test =['a','b','c']
new_str1 ='.'.join(test)
new_str2 = '|'.join(test)
print(new_str1)
print(new_str2)


sort_str ='a b d f m i p q c'
sort_list = sort_str.split()
print(sort_list)
sort_list.sort()
print(sort_list)
sort_str =''.join(sort_list)
print(sort_str)

# sorted()函数可以直接把字符串转换成列表并排序
sort_str_new ='abdfmipqc'
res = sorted(sort_str_new)
print(res)
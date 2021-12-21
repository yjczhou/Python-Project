# coding:utf-8

'''正则表达式的应用场景'''
# 判断一个字符串是否符合规则
# 去除指定数据
# 爬虫岗位较为核心的技术
# 彩票位置匹配彩票信息

'''正则表达式模块-re'''
import re

str_data = 'hello xiaomu,this is a good day!'

# search函数只能匹配一次
# (匹配规则，匹配字符串)
result = re.search('h([a-zA-Z])s',str_data)
# this
print(result.groups())

str_data = '本期彩票结果是:10,20,1,5,7,21,12'
# 匹配所有
result = re.findall('(\d+,\d+,\d+,\d+,\d+,\d+,\d+)',str_data)
print(result)

'''匹配字符串的需要条件'''
# 正则表达式模块--re
# 匹配的规则
# 字符串
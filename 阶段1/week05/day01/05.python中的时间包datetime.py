# coding:utf-8


'''
时间格式字符
字符            介绍
%Y          完成的年份
%m          月份（1-12）
%d          月中的某一天（1-31）
%H          一天中的第几个小时，24小时（00-23）

%I          一天中的第几个小时，12小时（01-12）
%M          当前的第几分（00-59）
%S          当前分的第几秒（0-61）闰年多占两秒
%f          当前秒的第多少毫秒

%a          简化的星期，如星期三 Wed
%A          完整的星期，如星期三 Wednesday
%b          简化的月份，如二月   Feb
%B          完整的月份，如二月   February

 %c          本地日期和时间，如Web Feb 5 10:14:49 2020
%p          显示上午还是下午，如AM代表上午，PM代表下午
%j          一年中的第几天
%U          一年中的星期数

'''


'''datetime包的常用功能'''
# 日期与时间的结合体 date and time
'''1.获取当前时间'''
# from datetime import datetime
# datetime.now()
# 或者
# import datetime
# datetime.datetime.now()

'''2.获取时间间隔'''
# from datetime import datetime
# from datetime import timedelta
# # 使用方法
# # 间隔天数   间隔秒数     间隔毫秒数     间隔微秒数    间隔分钟   间隔小时   间隔周数
# timeobj = timedelta(days=0,seconds=0,microseconds=0,milliseconds=0,
#                     minutes=0,hours=0,weeks=0)

'''3.将时间对象转成时间字符串'''
# # 获取时间
# from datetime import datetime
# now = datetime.now()
# # 时间转字符串
# date_str = now.strftime(format)

'''4.将字符串转成时间类型'''
# 获取时间模块
# from datetime import datetime
# 时间字符串转时间类型:
# datetime.strptime(tt,format)
# tt: 符合时间格式的字符串
# format：tt时间字符串匹配规则

'''datetime包的常用方法'''


'''datetime包的常用功能'''


# 获取当前时间
from datetime import date, datetime
now = datetime.now()
# datetime.datetime(2021, 12, 13, 17, 21, 41, 170994)
print(now,type(now))
# 2021-12-13 17:22:21.427537 <class 'datetime.datetime'>

# 获取时间间隔
# from datetime import datetime
from datetime import timedelta
# 使用方法
# 间隔天数   间隔秒数     间隔毫秒数     间隔微秒数    间隔分钟   间隔小时   间隔周数
one_day = timedelta(days=1)
# 昨天的这个时候，用减
yestoday = datetime.now() - one_day
# 后天就可以相加
print(yestoday)

# 将时间对象转换为时间字符串
# 获取时间
# from datetime import datetime
# now = datetime.now()
# 时间转字符串
date_str = now.strftime('%Y-%m-%d %H:%M:%S')
print(date_str,type(date_str))
# 2021-12-13 17:44:50 <class 'str'>

# 将时间字符串转为时间类型
str_date = '2021-10-10 13:13:13'
# 这里时间格式要一样
date_obj = datetime.strptime(str_date,'%Y-%m-%d %H:%M:%S')
print(date_obj,type(date_obj))
# 2021-10-10 13:13:13 <class 'datetime.datetime'>


'''datetime中生成时间戳函数'''
# from datetime import datetime
# 使用方法
now = datetime.now()
now_timestamp =  datetime.timestamp(now)
print(now_timestamp)
# now: datetime类型时间对象

'''datetime时间戳转时间对象'''
# from datetime import datetime
# 使用方法
# datetime.fromtimestamp(timestamp)
# tomestamp: 时间戳

datetime_obj = datetime.fromtimestamp(now_timestamp)
print(datetime_obj)


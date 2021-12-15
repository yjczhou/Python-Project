# coding:utf-8
'''认识时间戳'''
# 1970年1月1日00时00分00秒至今的总毫秒数
# timestamp表示时间戳
# float

'''time模块与他的函数们'''
# 时间处理，转换时间格式
# 生成时间戳函数time
# 获取本地时间函数localtime
# localtime对应字段介绍
# 暂停函数sleep
# time中的strftime与strptime


'''生成时间戳函数time'''
# 导入包
# import time
# 使用方法
# time.time()
# 返回值：
# 秒级别的浮点类型
# 举例
# 1580878485.4009378
import time
now = time.time()
print(now)

'''获取本地时间localtime'''
# 导入包
# import time

# 使用方法
# time.localtime(timestamp)
# 参数：timestamp：时间戳（可不传）

# import time
# 不传参数是指当前时间
# 传参数指的是对应时间戳的数据
t = time.localtime(now)
print(t)
# time.struct_time(tm_year=2021, tm_mon=12, tm_mday=13
# , tm_hour=18, tm_min=22, tm_sec=39, tm_wday=0, tm_yday=347
# , tm_isdst=0)

'''
localtime对应参数介绍
属性名      介绍            取值范围
tm_year     四位数年
tm_mon      月              1-12
tm_mday     日              1-31
tm_hour     小时            0-23
tm_min      分钟            0-59
tm_sec      秒              0-61 闰年多2秒
tm_wday     一周的第几天     0-6（0是周1）
tm_yday     一年的第几日    1-366（儒略历）
tm_isdst    夏令时          -1,0,1 是否是夏时令
'''


'''暂停函数sleep'''
# import time
# 使用方法
# time.sleep(second)
# second: 希望程序被暂停的秒数

# for i in range(10):
#     print(i)
#     time.sleep(1)# 每次暂停1秒
    
    

'''time中的strftime与strptime'''
# strftime()将time类型变成字符串类型
# import time
# 使用方法
# time.strftime(format,t)
# format: 格式化规范
# t: time.localtime对应的时间类型

str_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
print(str_time,type(str_time))

# strptime()将字符串对象变成时间对象
# import time
# 使用方法
# time.strptime(time_str,format)
# time_str: 符合时间格式的字符串
# format：确保与time_str一致的格式化标准

time_obj = time.strptime('2010-12-12','%Y-%m-%d')
print(time_obj)
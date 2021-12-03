# coding:utf-8

# 什么是格式化
# 一个固定的字符串中有部分元素是更具变量的值而改变的字符串

# 根据类型定义的格式化
# 字符串格式化使用操作符 % 来实现
# 对应格式符的变量，变量与格式符顺序一一对应，数量保持一致，超过1个格式化变量用小括号包裹。
# 数量不一致会报错
print('my name is %s' % ('dewei',))
print('my name is %s,my age is %s' % ('dewei',33))

books = ['python','django','flask']
info = 'my name is %s, my age is %s，my book is %s'
print(info % ('dewei',33,books))

dict = {
    'a':'a',
    'b':'b'
}
print('dict is %s' % dict)

# 字符串格式化函数format
# string.format() 函数用来格式化字符串
# string.format(data,data,data...)
print('hello {0},今天看起来气色{1}'.format('小慕','不错'))

# python3.6加入的新格式化方案  f-strings
# 定义一个变量
# 字符歘前加f符号
# 需要格式化的位置使用{变量名}
name = '小慕'
print(f'hello {name}')
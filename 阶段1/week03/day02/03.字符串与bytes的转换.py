# coding:utf-8

# 比特类型
# 二进制的数据流---bytes
# 一种特殊的字符串
# 字符串前 + b标记

bt = b'my name is dewei'
print(bt,type(bt))
print(bt.capitalize())
# print(bt.replace('xiaomu','dewei'))会报错
print(bt.replace(b'dewei',b'xiaomu'))#不会报错

print(bt[0])# 把对应字符转换为二进制位然后输出
print(bt[:3])
print(bt.find(b'm'))

'''dir内置函数 返回对象拥有的所有函数'''
print(dir(bt))

# c = b'hello 小慕'
# print(c)# 会报错 不能包含中文

'''encode()'''
# 将字符串转成比特(bytes)类型
# string.encode(encoding='utf-8',errors='strict')
# encoding: 转换成的编码格式，如ascii，gbk，默认utf-8
# errors：出错时的处理方法，默认strict，直接抛出错误，也可以选择ignore忽略错误
# 返回一个byte类型
str_data ='my name is dewei'
byte_data =str_data.encode('utf-8')
print(byte_data)

'''decode()'''
# 将比特类型转成字符串
# string.decode(encoding='utf-8',errors='strict')
# encoding: 转换成的编码格式，如ascii，gbk，默认utf-8
# errors：出错时的处理方法，默认strict，直接抛出错误，也可以选择ignore忽略错误
# 返回一个字符串类型
byte_data = b'python is a good code'
str_data = byte_data.decode('utf-8')
print(str_data)


# 所以上面的问题可以这样解决
c = 'hello 小慕'
d = c.encode()
print(d,type(d))
print(d.decode(),type(d.decode()))

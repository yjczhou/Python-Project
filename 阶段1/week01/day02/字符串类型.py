# coding:utf-8

safe = str('健康的体温是36.5')
name = '小慕'
# 都可以定义成字符串型

print(type(safe))
print(type(name))

# 字符串不可改变
# id() 返回变量的内存地址
print(id(name))
name = '小明'
print(id(name))

# len()返回字符串长度
print(len(name))

# 这种注释也可以赋值
info1 = '''今天天气真好呀'''
info2 = """你好"""
print(info1)
print(info2)
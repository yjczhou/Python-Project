# coding:utf-8

'''初识序列化'''
# 将对象信息，数据结构信息 通过一定规则进行转换，可以达到文件存储，或者网络传输的效果

'''可序列化的数据类型'''
# number
# str
# list
# tuple
# dict

'''不可序列化的数据类型'''
# set数据类型不能进行转换
# class
# def

'''python中的json模块

方法名      参数        介绍        举例                    返回值
dumps       obj         对象序列化  pickle.dumps([1,2])     比特
loads       byte        反序列化    pickle.loads('[1,2,3]') 原始数据类型
'''

import json
a = 1
b ='str'
c = [1,2,3]
d = (4,5,6)
e = {'name':'xiaomu'}
# 序列化
a_json = json.dumps(a)
b_json = json.dumps(b)
c_json = json.dumps(c)
d_json = json.dumps(d)
e_json = json.dumps(e)
print('------------------------')
print(a_json,type(a_json))
print(b_json,type(b_json))
print(c_json,type(c_json))
print(d_json,type(d_json))
print(e_json,type(e_json))
print(json.dumps(True),type(json.dumps(True)))
print(json.dumps(None),type(json.dumps(None)))
print('------------------------')
print(json.loads(a_json),type(json.loads(a_json)))
print(json.loads(b_json),type(json.loads(b_json)))
print(json.loads(c_json),type(json.loads(c_json)))
print(json.loads(d_json),type(json.loads(d_json)))
print(json.loads(e_json),type(json.loads(e_json)))
print(json.loads(json.dumps(True)),type(json.loads(json.dumps(True))))
print(json.loads(json.dumps(None)),type(json.loads(json.dumps(None))))

print('------------------------')
# pickie与json模块功能差不多，但json使用的较多
import pickle
pickle.dumps(e)
print(pickle.dumps(e))
print(pickle.loads(pickle.dumps(e)))
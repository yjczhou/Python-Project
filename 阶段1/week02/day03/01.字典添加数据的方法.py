# coding:utf-8

# []处理法
# 字典没有索引
# 通过key值修改或赋值
# 添加或修改，根据key是否存在所决定
d={'name':'dewei'}
d['name']='xiaomu'
print(d)

# updata函数
# 添加新的字典，如字典中有和原字典相同的key，则该key的value会被新字典的value覆盖
# dict.update(new_dict) new_dict为新的字典
default_dict ={'age':30}
new_dict ={'name':'dewei'}
default_dict.update(new_dict)
print(default_dict)

# setdefault函数
# 获取某个key的value，如key不存在于字典中，将会添加key并将value设为默认值
# value = dict.setdefault(key,value) key:需要获取的key，value: 如果key不存在，对应这个key存入字典的默认值
# 如果这个key存在于原本的字典中，则不会替换
default_dict ={}
value = default_dict.setdefault('name','dewei')
print('dict:',default_dict,'value:',value)

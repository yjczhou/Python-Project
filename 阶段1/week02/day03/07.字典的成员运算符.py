# coding:utf-8

# in,not in 只能判断key
test_dict = {'name':'xiaomu'}
print('name' in test_dict)
print('age' not in test_dict)
print('----------------------------------------')
# get
# 不存在默认返回None
# key存在则返回对应value
print(bool(test_dict.get('name')))
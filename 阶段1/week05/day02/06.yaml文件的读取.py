# coding:utf-8

'''yaml格式的介绍'''
# 文本文件
# 服务配置文件
# 基本格式如下
# name:                  key
#  xiaomu                value
# age:
#  10
# xinqing:               
#  -haha                 -列表
#  -heihei
# new:
#  a:b                   dict
#  c:1

'''Python的第三方模块 ---- pyyaml'''
# pip install pyyaml
# import yaml

'''读取yaml的方法'''
# 1.f = open(yaml_file,'r')
# 2.data = yaml.load(f.read())
# 3.f.close()
# 返回值： 字典类型
# 例如
# {
#     'name':'xiaomu',
#     'age':10,
#     'xinqing':['haha','heihei'],
#     'new':{'a':'b','c':1}
# }

import yaml


def read(path):
    with open(path,'r',encoding='utf-8') as f:
        data = f.read()
    # 三种方法选择一种即可
    # result = yaml.load(data,Loader=yaml.FullLoader)
    # result = yaml.load(data,Loader=yaml.CLoader)
    result = yaml.safe_load(data)
    f.close()
    return result

if __name__ == '__main__':
    result = read('muke.yaml')
    print(result)

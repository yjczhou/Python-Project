# coding:utf-8

import re

def had_numbers(data):
    result = re.findall('\d',data)
    print(result)
    if len(result) != 0:
        return True
    else: 
        return False

def remove_numbers(data):
    # 匹配非数字
    result = re.findall('\D',data)
    print(result)
    return ''.join(result)

def startswith(sub,data):
    _sub = '\A'+sub
    result = re.findall(_sub,data)
    # 如果列表里有值，就会进行循环，没有值就会返回False
    for i in result:
        return True
    else:
        return False
    
def endswith(sub,data):
    _sub = sub + '\Z'
    result = re.findall(_sub,data)
    if len(result) != 0:
        return True
    else: 
        return False

# 去除空格后的长度
def real_len(data):
    result = re.findall('\S',data)
    print(result)
    return len(result)

if __name__ == '__main__':
    data = 'i am dewei, i am 33'
    result = had_numbers(data)
    print(result)
    result = remove_numbers(data)
    print(result)
    
    data = 'hello xiaomu, i am dewei. i am 33 year\'s old'
    print(re.findall('\W',data))
    # [' ', ',', ' ', ' ', ' ', '.', ' ', ' ', ' ', ' ', "'", ' ']
    
    result = startswith('hell',data)
    print(result)
    result = endswith('old',data)
    print(result)
    
    print(len(data))
    result = real_len(data)
    print(result)
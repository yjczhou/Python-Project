# coding:utf-8

'''base64包介绍'''
# 通用型
# 可解密

'''base64包常用方法
函数名          参数    介绍                举例                                返回值
encodestring    Byte    进行base64加密      base64.encodestring(b'hello')       byte
decodestring    Byte    对base64解密        base64.decodestring(b'eGlhb211\n')  byte

encodebytes     Byte    进行base64加密      base64.encodebytes(b'py')           byte
decodebytes     Byte    对base64解密        base64.decodebytes(b'eGlhb211\n')   byte
'''

import base64

replace_one = '%'
replace_two = '$'

# 封装encode
def encode(data):
    if isinstance(data,str):
        # 转byte
        data = data.encode('utf-8')
    elif isinstance(data,bytes):
        data = data
    else:
        raise TypeError('data need bytes or str')
    
    # 加密后的字符串是byte型，但是字符串操作方便，所以转换成字符串类型
    # return base64.encodebytes(data).decode('utf-8')
    
    # 优化
    # 因为别人可以直接解密，所以我们可以二次输出
    _data = base64.encodebytes(data).decode('utf-8')
    _data = _data.replace('a',replace_one).replace('2',replace_two)
    return _data

# 封装decode
def decode(data):
    if not isinstance(data,bytes):
        raise TypeError('data need bytes')
    
    # 优化
    replace_one_b = replace_one.encode('utf-8')
    replace_two_b = replace_two.encode('utf-8')
    data = data.replace(replace_one_b,b'a').replace(replace_two_b,b'2')
    
    
    # 对加密后的比特数据解密，然后转成字符串
    return base64.decodebytes(data).decode('utf-8')

if __name__ == '__main__':
    # 加密
    result = encode('hello xiaomu')
    print(result)
    # aGVsbG8geGlhb211
    
    # 解密
    new_result = decode(result.encode('utf-8'))
    print(new_result)
# coding:utf-8

'''python中加密工具'''

'''hashlib包介绍'''
# 难破解
# 不可逆
'''hashlib中常用加密方法
函数名      参数        介绍            举例                        返回值
md5         byte        Md5算法加密     hashlib.md5(b'hello')       Hash对象
sha1        byte        Sha1算法加密    hashlib.sha1(b'hello')      Hash对象
sha256      byte        Sha256算法加密  hashlib.sha256(b'hello')    Hash对象
sha512      byte        Sha512算法加密  hashlib.sha512(b'hello')    Hash对象
'''

import hashlib
# 示例
# 生成加密字符串
hashobj = hashlib.md5(b'hello')
# 将加密对象按照16进制生成加密字符串
result = hashobj.hexdigest()
print(result)
# 5d41402abc4b2a76b9719d911017c592

# 使用场景
import time
# 共识，也叫公钥
base_sign = 'muke'

def custom():
    # 时间戳
    a_timestamp = int(time.time())
    #客户端计算的token 
    _token = '%s%s' % (base_sign,a_timestamp)
    # print(_token)
    # 转比特类型
    hashobj = hashlib.sha1(_token.encode('utf-8'))
    # 客户端加密后的token
    a_token = hashobj.hexdigest()
    # 进行多值返回
    return a_token,a_timestamp

def b_service_check(token,timestamp):
    # 利用共识与a的时间戳 
    # 服务端自己计算的token
    _token = '%s%s' % (base_sign,timestamp)
    # 服务端加密后的token
    b_token = hashlib.sha1(_token.encode('utf-8')).hexdigest()
    # 进行比对
    if token == b_token:
        return True
    else:
        return False

if __name__ == '__main__':
    # 获得返回的两个参数
    # 如果只有一个参数接受，则会转换为一个元组，将返回的多个数据存入元组中
    # 客户端token与时间戳
    need_help_token,timestamp = custom()
    
    # 如果服务端使用自己的时间戳，因为执行时间很短，所以还是会合法
    # 我们可以使用sleep函数,进行延时操作
    time.sleep(1)
    
    # 进行token比对
    result =b_service_check(need_help_token,int(time.time()))
    if result == True:
        print('a合法，b服务可以进行帮助')
    else:
        print('a不合法，b服务不可以进行帮助')

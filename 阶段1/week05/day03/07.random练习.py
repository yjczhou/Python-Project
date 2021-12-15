# coding:utf-8

import random
from typing import Counter

gifts = ['iphone','ipad','car','tv']

def chioce_gifts():
    gift = random.choice(gifts)
    print(f'你得到了{gift}')


# 这个函数增加了中奖的概率
def chioce_gift_new():
    # 在0-99随机返回一个数字
    count = random.randrange(0,100,1) 
    if  0< count <= 50:  # 50%
        print('你中了一个iPhone')
    elif count <= 70: # 20%
        print('你中了一个ipad')
    elif count <= 90: # 20%
        print('你中了一个tv电视')
    else: # 10%
        print('你中了一辆车')


if  __name__ == '__main__':
    # chioce_gifts()
    chioce_gift_new()
# coding:utf-8

""" 
    1.User类的初始化
    2.get_user(时间的转变)
    3.查看奖品列表
"""
''''
    1.抽奖函数 随机判断第一层（level1）1:50%  2:30%  3:15%  4:5%
    2.抽奖函数 随机判断第二层（level2）1:80%  2:15%  3:5%
    3.抽奖函数 获取对应层级的真实奖品，并随机一个奖品，查看奖品count是否为0
                不为0 中奖  提示用户，并奖品数量-1，并为用户更新
                奖品到user表中的gifts中
                数量为0，则未中奖
'''
import os
import random
from base import Base
from common.error import NotUserError,RoleError,UserActiveError,CountError
from common.utils import timestamp_to_string

class User(Base):
    def __init__(self,username,user_json,gift_json):
        self.username = username
        self.gift_random = list(range(1,101))
        super(User, self).__init__(user_json,gift_json)
        self.get_user()

    def get_user(self):
        users = self._Base__read_users()
        
        if self.username not in users:
            raise NotUserError('not user %s' % self.username)
        
        current_user = users.get(self.username)
        
         # 判断用户是否被冻结
        if current_user.get('active') == False:
            raise UserActiveError('the user %s had not use'% self.username)
        
        # 如果不是普通用户
        if current_user.get('role') != 'normal':
             raise RoleError('permission by normal')
        
        self.user = current_user
        self.role = current_user.get('role')
        self.name = current_user.get('username')
        self.gifts = current_user.get('gifts')
        self.create_time = timestamp_to_string(current_user.get('create_time'))
    def get_gifts(self):
        gifts = self._Base__read_gifts()
        # print(gifts)
        gift_lists = []
        # level_one是对应键,level_one_pool对应值
        # 遍历一级
        for level_one,level_one_pool in gifts.items():
            # 遍历二级
            for level_two,level_two_pool in level_one_pool.items():
                # 遍历礼品
                for gift_name in level_two_pool:
                    gift_lists.append(gift_name)
        return gift_lists
    
    
    def chioce_gift(self):
        self.get_user()
        first_level = None
        # level1
        # 在1-100之间随机选择一个数
        level_one_count = random.choice(self.gift_random)
        # print(level_one_count)
        if 1<= level_one_count <= 50:
            first_level = 'level1'
        elif level_one_count <= 80:
            first_level = 'level2'
        elif level_one_count <95:
            first_level = 'level3'  
        elif level_one_count >= 95:
            first_level = 'level4'
        else:
            raise CountError('level_one_count need 0-100')
        
        gifts = self._Base__read_gifts()
        # 我们得到了 第一次随机选择的
        level_one = gifts.get(first_level)
        # print(level_one)
        
        # level2
        second_level = None 
        level_two_count = random.choice(self.gift_random)
        # print(level_two_count)
        if 1<= level_two_count <= 80:
            second_level = 'level1'
        elif level_two_count < 95:
            second_level = 'level2'
        elif level_two_count >= 95:
            second_level = 'level3'  
        else:
            raise CountError('level_two_count need 0-100')
        # 我们得到了 第二层的随机数据
        level_two = level_one.get(second_level)
        print(level_two)
        if len(level_two) == 0:
            print('哦可惜，你没有中奖')
            return
        
        # 这一级的奖品
        gift_names = []
        # 
        for k,v in level_two.items():
            gift_names.append(k)
        
        # 随机选择列表中的奖品  
        gift_name = random.choice(gift_names)
        # 判断是否有库存
        gift_info = level_two.get(gift_name)
        
        if gift_info.get('count') <= 0:
            print('哦可惜，你没有中奖')
            return
        else:
            # 从库存中删除一件这个物品
            gift_info['count'] -= 1
            level_two[gift_name] = gift_info
            level_one[second_level] = level_two
            gifts[first_level] = level_one
            self._Base__save(gifts,self.gift_json)
            self.user['gifts'].append(gift_name)
            self.update()
            print('恭喜你，你中了一个%s' % gift_name)
    
    def update(self):    
        users = self._Base__read_users()
        users[self.username] = self.user
        self._Base__save(users,self.user_json)
        
        
if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), 'storage','gift.json')
    user_path = os.path.join(os.getcwd(), 'storage','user.json')
    user = User('小慕',user_path,gift_path)
    # print(user.name,user.create_time,user.gifts,user.role)
    # print( user.get_gifts())
    user.chioce_gift()
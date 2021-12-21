# coding:utf-8

""" 
    1.导入user.json 文件检查
    2.导入gift.json 文件检查  
"""
'''
    1.确定用户表中每个用户的信息字段
    2.读取user.json文件
    3.读取gift.json文件
    
    username 姓名
    role 权限 normal admin
    active 活跃的 True False
    create_time 注册时间
    update_time 修改时间
    gifts []
    {username:{username,active...}}
'''
'''
    1.role的修改
    2.active的修改
    3.delete_user
'''
'''
    1.gifts 奖品结构的确定
    2.gifts 初始化
    3.gifts 奖品的读取
    4.gifts 添加
    
    {
        level1:{
            同一个级别里也有概率之分
            level1:{
                gift_name1:{
                    name:xx
                    count:xx
                },
                gift_name2:{}
            },
            level2:{},
            level3:{}
        },
        level2:{
            level1:{}
            level2:{}
            level3:{}
        },
        level3:{
            level1:{}
            level2:{}
            level3:{}
        }
    }
'''
import os
import json
import time
from common.error import UserExitsError,RoleError,LevelError,NagativeNumberError,CountError
from common.utils import check_file,timestamp_to_string
from common.consts import ROLES,FIRSTLEVELS,SECONDLEVELS
class Base(object):
    def __init__(self,user_json,gift_json):
        self.user_json = user_json
        self.gift_json = gift_json
        
        # 调用__check_user_json
        # 检测文件是否存在
        self.__check_user_json()
        self.__check_gift_json()
        # 初始化礼物
        self.__init_gifts()
    
    def __check_user_json(self):
        check_file(self.user_json)
        
    def __check_gift_json(self):
        check_file(self.gift_json)
        
    def __read_users(self,time_to_str = False):
        with open(self.user_json, 'r') as f:
            # 读取的是json数据
            # 反序列化
            # 变成字典
            data = json.loads(f.read())
            # print(data,type(data))
        if time_to_str:
            for username,v in data.items():
                v['create_time'] = timestamp_to_string(v['create_time'])
                v['update_time'] = timestamp_to_string(v['update_time'])
                data[username] = v
        return data
    
    def __write_user(self,**user):
        # print(user)
        if 'username' not in user:
            raise ValueError('missing username')
        
        if 'role' not in user:
            raise ValueError('missing role')
        user['active'] = True
        user['create_time'] = time.time()
        user['update_time'] = time.time()
        user['gifts'] = []
        
        # 接受的是一个字典
        users = self.__read_users()
        if user['username'] in users:
            raise UserExitsError('username %s had exists' % user['username'])
        
        # 更新用户字典
        # 以用户名为key
        users.update(
            {user['username']:user}
        )
        self.__save(users,self.user_json)
    
    # 修改角色信息
    def __change_role(self,username,role):
        # 读取全部用户信息
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False
        if role not in ROLES:
            raise RoleError('not use role %s' % role)
        else:
            user['role'] = role
            user['update_time'] = time.time()
            
            # 把修改后的对象赋值1
            users[username] = user
        
        self.__save(users,self.user_json)
        return True
        
    # 修改活跃信息
    def __change_active(self, username):
         # 读取全部用户信息
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False
        
        user['active'] = not user['active']
        user['update_time'] = time.time()
        users[username] = user
        
        self.__save(users,self.user_json)
        return True
    
    def __delete_user(self,username):
         # 读取全部用户信息
        users = self.__read_users()
        user = users.get(username)
        if not user:
            return False
        
        delete_user = users.pop(username)
        
        self.__save(users,self.user_json)
        # 返回被删除的value
        return delete_user
    
    # 读取礼物
    def __read_gifts(self):
        with open(self.gift_json,'r') as f:
            # 序列化
            data = json.loads(f.read())
        return data    
    
    # 初始化礼物
    def __init_gifts(self):
        data = {
           'level1':{
               'level1':{},
               'level2':{},
               'level3':{}
           },
           'level2':{
               'level1':{},
               'level2':{},
               'level3':{}
           },
           'level3':{
               'level1':{},
               'level2':{},
               'level3':{}
           },
           'level4':{
               'level1':{},
               'level2':{},
               'level3':{}
           }
        }
        gifts = self.__read_gifts()
        if len(gifts) != 0:
           return

        self.__save(self,data,self.gift_json)
            
    #写入奖品 
    def __write_gift(self,first_level,second_level,gift_name,gift_count):
        
        # 验证输入的级别是否存在
        if first_level not in FIRSTLEVELS:
            raise LevelError('first_level not exists %s' % first_level)
        if second_level not in SECONDLEVELS:
            raise LevelError('second_level not exists %s' % second_level)

        if gift_count <= 0:
            gift_count = 1
        # 读取礼品
        gifts = self.__read_gifts()
        # 一级奖池
        current_gift_pool = gifts[first_level]
        # 二级奖池
        current_second_gift_pool = current_gift_pool[second_level]
        
        # 如果有就直接加数量
        if gift_name in current_second_gift_pool:
            current_second_gift_pool[gift_name]['count'] = current_second_gift_pool[gift_name]['count'] + gift_count
        else:
            # 没有就添加
            current_second_gift_pool[gift_name] = {
                    'name':gift_name,
                    'count':gift_count
            }
        # 把奖品添加二级奖品中  
        current_gift_pool[second_level] = current_second_gift_pool
        # 把二级奖池添加到一级奖池中
        gifts[first_level] = current_gift_pool
        self.__save(gifts,self.gift_json)
        
    # 修改奖品数量，不传gift_count就奖品减1
    def __gift_update(self,first_level,second_level,gift_name,gift_count=1,is_admin=False):
         
        assert isinstance(gift_count,int),'gift count is a int'

        result = self.__check_and_getgift(first_level,second_level,gift_name)
        if result == False:
            return result
        
        current_gift = result['level_two'][gift_name]
        
        # 拥有管理员权限
        if is_admin == True:
            if gift_count <= 0 :
                raise CountError('gift count not 0')
            # 管理员可以直接修改奖品数量，不管是增多还是减少
            current_gift['count'] = gift_count
            
        else:
            # 如果没有管理员权限，就只能减少礼品数量
            # 数量不满
            if current_gift['count'] - gift_count < 0:
                raise NagativeNumberError('gift count can not negative')

            current_gift['count'] = current_gift['count'] - gift_count
        
        # 给gift_name
        result['level_two'][gift_name] = current_gift
        # 给二级菜单
        result['level_one'][second_level] = result['level_two']
        # 给一级菜单
        result['gifts'][first_level] =  result['level_one']
        
        self.__save(result['gifts'],self.gift_json)
    
    # 删除奖品
    def __delete_gift(self,first_level,second_level,gift_name):
        
        result = self.__check_and_getgift(first_level,second_level,gift_name)
        
        if result == False:
            return result
        
        # 返回删除的数据
        delete_gift_data = result['level_two'].pop(gift_name)
           
        result['level_one'][second_level] = result['level_two']
        
        result['gifts'][first_level] =  result['level_one']

        self.__save(result['gifts'],self.gift_json)
        return delete_gift_data
    
    
    def __check_and_getgift(self,first_level,second_level,gift_name):
         # 验证输入的级别是否存在
        if first_level not in FIRSTLEVELS:
            raise LevelError('first_level not exists %s' % first_level)
        if second_level not in SECONDLEVELS:
            raise LevelError('second_level not exists %s' % second_level)

        # 读取礼品
        gifts = self.__read_gifts()
         # 一级奖池
        level_one= gifts[first_level]
        # 二级奖池
        level_two = level_one[second_level]
        
        if gift_name not in level_two:
            return False
        return {'level_one':level_one,'level_two':level_two,'gifts':gifts}
    # 把数据写入文件中
    def __save(self,data,path):
        json_data = json.dumps(data)
        with open(path,'w') as f:
            f.write(json_data)

if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), 'storage','gift.json')
    user_path = os.path.join(os.getcwd(), 'storage','user.json')
    # print(gift_path)
    # print(user_path)
    base = Base(user_json=user_path,gift_json=gift_path);
    # base._Base__write_user(username='dewei',role = 'admin')
    # print()
    # result = base.change_role(username='dewei',role='normal')
    # print(result)
    
    # result = base.change_active(username='dewei')
    # result = base.delete_user(username='dewei')
    # print(result)
    base._Base__write_gift(first_level='level1',second_level='level1',gift_name='iphoneX',gift_count=10)
    
    # print(result)
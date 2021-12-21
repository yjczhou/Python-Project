# coding:utf-8

'''
    1.admin类的创建
    2.获取用户函数(包括获取身份)
    3.添加用户(判断当前身份是否是管理员)
    4.冻结与恢复用户
    5.修改用户身份
'''
'''
    1.admin的验证(只有admin的用户才能用这个类)
    2.任何函数都应该动态的更新getuser
    3.奖品的添加
    4.奖品的删除
    5.奖品数量的更新（同步base调整）
'''
import os
from base import Base
from common.error import NotUserError,UserActiveError,RoleError


class Admin(Base):
    def __init__(self,username,user_json,gift_json):
        self.username = username
        # 执行父类的构造函数
        super(Admin,self).__init__(user_json,gift_json)
        
        self.get_user()
    
    # 得到所有用户
    def get_user(self):
        # 调用父类的这个函数,获得用户数据
        users = self._Base__read_users()
        current_user = users.get(self.username)
        
        # print(current_user)
        if current_user  == None:
            raise NotUserError('not user %s' % self.username)
        
        # 判断用户是否被冻结
        if current_user.get('active') == False:
            raise UserActiveError('the user %s had not use'% self.username)
        
        if current_user.get('role') != 'admin':
            raise RoleError('permission by admin')
            
        self.user = current_user
        self.role = current_user.get('role')
        self.name = current_user.get('username')
        self.active = current_user.get('active')   
    
    # 添加用户
    def add_user(self, username,role):
        self.__check('permission')
        self._Base__write_user(username=username, role=role) 
    
    # 更新用户状态
    def update_users_active(self, username):
        self.__check('permission')
        self._Base__change_active(username=username)
    
    # 更新用户角色
    def update_users_role(self,username,role):
        self.__check('permission')
        self._Base__change_role(username=username,role=role)  
    
    # 添加礼品
    def add_gift(self,first_level,second_level,gift_name,gift_count):
        self.__check('permission')
        self._Base__write_gift(first_level,second_level,gift_name,gift_count)
    
    
    # 奖品的删除
    def delete_gift(self,first_level,second_level,gift_name):
        self.__check('permission')
        self._Base__delete_gift(first_level,second_level,gift_name)


    # 更新奖品信息
    def update_gift(self,first_level,second_level,gift_name,gift_count):
        self.__check('permission')
        self._Base__gift_update(first_level,second_level,gift_name,gift_count,is_admin=True)
    
    # 
    def __check(self,message):
        self.get_user()
        if self.role != 'admin':
            raise Exception(message)
    
if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), 'storage','gift.json')
    user_path = os.path.join(os.getcwd(), 'storage','user.json')
    
    # 实例化dewei管理员类
    admin = Admin('小慕',user_path,gift_path)
    # print(admin.name,admin.role)
    # admin.update_users_role(username='小慕',role='normal')
    admin.update_gift('level1','level2','iphone10',100)
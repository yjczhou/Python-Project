# coding:utf-8

'''学生信息库'''
# 升级，使用类的形式
class StudentInfo(object):
    def __init__(self,students):
        self.students =students
    
    # 通过id查询具体用户信息
    def get_by_id(self,student_id):
        if student_id not in self.students:
            print('没有该学生信息')
        else:
            result = self.students.get(student_id)
            print('查询信息为: 学号:{},姓名:{},年龄:{},班级:{},性别:{}'\
                    .format(student_id,result['name'],result['age'],result['class_number'],result['sex']))
    
    # 查看所有学生的信息
    def get_all(self):
        for id_,value in self.students.items():
            print('学号:{},姓名:{},年龄:{},班级:{},性别:{}'\
                .format(id_,value['name'],value['age'],value['class_number'],value['sex'])) 
        return self.students
    # 添加学生的信息
    def add(self,**student):
        check =  self.check_user_info(**student)
        if check!=True:
            print('添加失败:',check)
            return
        # d={'1':'6','2':'5','3':'4'}
        # 1、max() 函数中没有 key 参数时，求的是 key 的最大值
        # print(max(d))
        # 2、max() 函数中有 key 参数时，求的是 value 的最大值
        # print(max(d,key=d.get()))
        self.__add(**student)
        print('添加成功')
        self.get_all()
        return self.students
    # 批量添加功能
    def adds(self,new_students):
        for student in new_students:
            # 检查每一项是否合法
            check = self.check_user_info(**student)
            if check!=True:
                print('添加失败:',check,student.get('name'))
                # 不合法就打断本次循环，执行下一次循环
                continue
            # 调用私有函数处理添加功能
            self.__add(**student)
        print('批量添加成功')
        self.get_all()
    
    # 定义私有函数，处理添加功能
    def __add(self,**student):
        new_id = max(self.students)+1
        self.students[new_id] = student      
        
    # 删除学生信息
    def delete(self,student_id):
        if student_id not in self.students:
            print('学生的学号{}不存在'.format(student_id))
            return
        else:
            # 删除字典中指定的key，并将其结果返回，如果key不存在则报错
            # value = dict.pop(key) key 要删除的键 返回被删除的value
            userInfo = self.students.pop(student_id)
            # print(userInfo)
            print('学号是{}，{}同学的信息已经被删除了'.format(student_id,userInfo['name']))
    
    # 批量删除函数
    def deletes(self,ids):
        for id_ in ids:
            if id_ not in self.students:
                print('学生的学号{}不存在'.format(id_))
                continue
            student_Info = self.students.pop(id_)
            print(f'学号{id_},学生{student_Info["name"]}已被移除')
        print('批量删除成功')
        self.get_all()
               
    # 修改学生的信息
    def update(self,student_id,**kwargs):
        if student_id not in self.students:
            print('没有这个学生信息')
            return
        else:
           self.__update(student_id,**kwargs)
        print('修改成功')
        self.get_all()
        return self.students
    # 批量更新
    def updates(self,update_students):
        for student in update_students:
            # print(student)
            id_ = list(student.keys())[0]
            # print(id_)
            if id_ not in self.students:
                print('没有这个学生信息')
                continue
            self.__update(id_,**student[id_])
        print('批量修改成功')
        self.get_all();
    
    # 定义私有函数，处理修改功能
    def __update(self,id_,**student):
        if 'name' in student:
            self.students[id_]['name'] =student['name']
        if 'age' in student:
            self.students[id_]['age'] =student['age']
        if 'class_number' in student:
            self.students[id_]['class_number']=student['class_number']
        if 'sex' in student:
            self.students[id_]['sex'] =student['sex']
    # 查询信息
    # 优化函数，支持模糊匹配  
    def search_users(self,**kwargs):
        values = list(self.students.values())
        key = None
        value = None
        result =[]
        if 'name' in kwargs:
            key = 'name'
        elif 'sex' in kwargs:
            key = 'sex'
        elif 'class_number' in kwargs:
            key = 'class_number'
        elif 'age' in kwargs:
            key = 'age'
        else:
            print('没有发现搜索的关键字')
            return
        value = kwargs[key]
        # values里面每一个都是一个对象
        for user in values:
            if value in user[key]:
                result.append(user)
        return result
    # 检查用户信息
    def check_user_info(self,**kwargs):
        if 'name' not in kwargs:
            return '没有发现学生姓名'
        if 'age' not in kwargs:
            return '没有发现学生年龄'
        if 'class_number' not in kwargs:
            return '没有发现学生班级'
        if 'sex' not in kwargs:
            return '没有发现学生性别'
        return True
        

students ={
    1:{
        'name':'dewei',
        'age':33,
        'class_number':'A',
        'sex':'boy'
    },
    2:{
        'name':'小慕',
        'age':10,
        'class_number':'B',
        'sex':'boy'
    },
    3:{
        'name':'小曼',
        'age':18,
        'class_number':'A',
        'sex':'girl'
    },
    4:{
        'name':'小高',
        'age':18,
        'class_number':'C',
        'sex':'boy'
    },
    5:{
        'name':'小云',
        'age':18,
        'class_number':'B',
        'sex':'girl'
    },
}
# d = {'name':'小慕','age':10}
# d_items = d.items()
# print(d_items)
# dict_items([('name', '小慕'), ('age', 10)])

# 字典利用items内置函数进行for循环
# 将字典转成为列表，每个key，value转成元组
# for key,value in dict.items():
#   print(key,value)
# key: for循环体中获取的字典当前元素的key
# value：for循环体中对应当前key的值的value
# items()返回一个伪列表
# 获取所有信息

# student_list = students.items()
# print(student_list)


# get_all_student()


# add_student(name='小白',age=19,class_number = 'A',sex='boy')




# delete_student(6)



# update_student(6,name='小红',age=20)
# get_all_student()


# get_user_by_id(2)


# user = 
# print(user)

if __name__ == '__main__':
    # 实例化对象
    student_info = StudentInfo(students)
    # 查看所有用户信息
    student_info.get_all()
    print('------------------------------------------------')
    # 根据用户id查看用户信息
    student_info.get_by_id(1)
    print('------------------------------------------------')
    # 添加一个用户
    student_info.add(name='小白',age=19,class_number = 'A',sex='boy')
    print('------------------------------------------------')
    # 批量添加用户
    users = [
        {'name':'xiaoming','age':17,'class_number':'B','sex':'boy'},
        {'name':'xiaohong','age':18,'class_number':'C','sex':'girl'},
    ]
    student_info.adds(users)
    print('------------------------------------------------')
    # 批量删除
    ids =[7,8]
    student_info.deletes(ids)
    print('------------------------------------------------')
    # 批量修改
    update_users=[
        {5:{'name':'xiaoyun','age':20,}},
        {6:{'name':'xaiobai','sex':'girl'}}
        ]
       
    student_info.updates(update_users)
    # student_info.update(6,name='小红',age=20)
    print('------------------------------------------------')
    # 模糊查找
    # 如果想用年龄字段模糊查找，需要把年龄字段改成str类型
    result = student_info.search_users(name = 'a')
    print(result)
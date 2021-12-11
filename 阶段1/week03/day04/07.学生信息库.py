# coding:utf-8

'''学生信息库'''

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

def get_all_student():
    for id_,value in students.items():
        print('学号:{},姓名:{},年龄:{},班级:{},性别:{}'\
              .format(id_,value['name'],value['age'],value['class_number'],value['sex'])) 
    return students
# get_all_student()

def add_student(**kwargs):
    if 'name' not in kwargs:
        print('没有发现学生姓名')
        return
    if 'age' not in kwargs:
        print('没有发现学生年龄')
        return
    if 'class_number' not in kwargs:
        print('没有发现学生班级')
        return
    if 'sex' not in kwargs:
        print('没有发现学生性别')
        return
    # d={'1':'6','2':'5','3':'4'}
    # 1、max() 函数中没有 key 参数时，求的是 key 的最大值
    # print(max(d))
    # 2、max() 函数中有 key 参数时，求的是 value 的最大值
    # print(max(d,key=d.get()))
    id_ = max(students) + 1
    students[id_]={
        'name':kwargs['name'],
        'age':kwargs['age'],
        'class_number':kwargs['class_number'],
        'sex':kwargs['sex']
    }
    return students
add_student(name='小白',age=19,class_number = 'A',sex='boy')

# 删除学生的信息
def delete_student(student_id):
    if student_id not in students:
        print('学生的学号{}不存在'.format(student_id))
        return
    else:
        # 删除字典中指定的key，并将其结果返回，如果key不存在则报错
        # value = dict.pop(key) key 要删除的键 返回被删除的value
        userInfo = students.pop(student_id)
        # print(userInfo)
        print('学号是{}，{}同学的信息已经被删除了'.format(student_id,userInfo['name']))

# delete_student(6)

# 修改学生的信息
def update_student(student_id,**kwargs):
    if student_id not in students:
        print('没有这个学生信息')
        return
    else:
        if 'name' in kwargs:
            students[student_id]['name'] =kwargs['name']
        if 'age' in kwargs:
            students[student_id]['age'] =kwargs['age']
        if 'class_number' in kwargs:
            students[student_id]['class_number']=kwargs['class_number']
        if 'sex' in kwargs:
            students[student_id]['sex'] =kwargs['sex']
    print('修改成功')
    return students

update_student(6,name='小红',age=20)
# get_all_student()

# t通过id查询具体用户信息
def get_user_by_id(student_id):
    if student_id not in students:
        print('没有该学生信息')
    else:
        result = students.get(student_id)
        print('学号:{},姓名:{},年龄:{},班级:{},性别:{}'\
                .format(student_id,result['name'],result['age'],result['class_number'],result['sex']))
# get_user_by_id(2)

# 查询信息
def search_user(**kwargs):
    values = list(students.values())
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
    for user in values:
        if user[key] == value:
            result.append(user)
    return result
# user = search_user(age = 18)
# print(user)

print(students.keys()) 
        
from re import U
import mongoengine

from user import User, Address,Hobby


# 连接数据库
def setup():
    mongoengine.register_connection(
        alias='core',
        db='demo',
        host='127.0.0.1',
        port=27017,
        # 验证
        username="zhou",
        password="1234"
    )


def print_header():
    print('----------------------------------------------')
    print('|                                             |')
    print('|           User Management v.02              |')
    print('|               demo edition                  |')
    print('|                                             |')
    print('----------------------------------------------')
    print()


def user_loop():
    while True:
        print("Available actions:")
        print(" * [a]dd user")
        print(" * [l]ist users")
        print(" * [u]pdate password")
        print(" * [d]elete user")
        print(" * e[x]it")
        print()
        ch = input("> ").strip().lower()
        if ch == 'a':
            add_user()
        elif ch == 'l':
            list_users()
        elif ch == 'u':
            update_users()
        elif ch == 'd':
            delete_user()
        elif not ch or ch == 'x':
            print("Goodbye")
            break


def add_user():
    username = input("username = ")
    password = input("password = ")
    email = input("email = ")
    age = input("age = ")
    
    # 嵌套Document的实现 对象形式
    city = input("city = ")
    zip_code = input("zip code =")
    

    # 实例化User对象，为其赋值
    user = User()
    user.username = username
    user.password = password
    user.email = email
    user.age = age
    
    # 把嵌套字段添加到user里
    address = Address()
    address.city = city
    address.zip_code = zip_code
    user.address = address

    # 嵌套Document的实现 列表形式
    # 实例化的Hobby都是嵌套的对象形式
    h1 = Hobby()
    h1.type = "reading"
    h1.rating = 10
    h2 = Hobby()
    h2.type = "writing"
    user.hobbies = [h1,h2]
    
    # 数据的插入
    user.save()


def list_users():
    # User.objects()获取users集合的所有数据，返回一个可迭代的结果
    users = User.objects()
    for u in users:
        print('username={},password={},age={}'.format(u.username,u.password, u.age))

    '''普通字段过滤查询'''
    # 但是如果我们想对结果进行过滤该如何操作,
    # 会返回username="zhou"的一条对象
    # users = User.objects(username="zhou")
    # for u in users:
    #     print('username={},age={}'.format(u.username, u.age))
        
    # 如何使用过滤运算符
    # 在对应字段名后加__ 和运算符
    # 返回年龄小于18的
    # users = User.objects(age__lte=18)
    # # 返回年龄在18或21的
    # users = User.objects(age__in=[18,21])
    # for u in users:
    #     print('username={},age={}'.format(u.username, u.age))
    
    '''嵌套字段查询''' 
    # 查询usera集合里address字段里city等于china的数据
    # users = User.objects(address__city='china')
    # for u in users:
    #     print('username={},age={}'.format(u.username, u.age))
    
    # 查询usera集合里hobbies字段里数据中的type等于reading的数据 
    # 执行 $elemMatch 以便您可以匹配数组中的整个文档
    # users = User.objects(hobbies__match={"type":"reading"})
    # for u in users:
    #     print('username={},age={}'.format(u.username, u.age))
    
    '''对获取的数据进行排序'''
    # 按照age字段进行排序，默认升序，
    # users = User.objects().order_by('age')
    # 在字段名前加一个“-”
    # users = User.objects().order_by('-age')
    # 其实我 们可以给users一个默认的排序，在user.py中meta中设置
    # users = User.objects()
    
    # first()选择第一条数据
    # user = User.objects().first()
    # print('username={},age={}'.format(user.username, user.age))
    
    # 取前两条数据,可以利用切片来实现
    # 我们也可以利用切条来实现跳过数据的功能,如[2:4]
    # users = User.objects()[:2]
    # for u in users:
    #     print('username={},age={}'.format(u.username, u.age))
        

# 修改密码
def update_users():
    username = input('username = ')
    # 通过用户名查找用户,取第一个用户
    user = User.objects(username=username).first();
    if not user:
        print('user %s not exist'.format(username))
        return
    else:
        password = input('new password =')
        user.password = password
        # 在数据库中保存
        user.save()

# 删除用户
def delete_user():
    username = input('username = ')
    # 通过用户名查找用户,取第一个用户
    user = User.objects(username=username).first();
    if not user:
        print('user %s not exist'.format(username))
        return
    else:
        # 在数据库删除用户
        user.delete()
           
        
if __name__ == "__main__":
    setup()
    print_header()
    user_loop()

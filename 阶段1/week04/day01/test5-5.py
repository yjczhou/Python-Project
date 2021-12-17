class Person(object):
# 重写实例对象的构造（初始化）方法
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
# 自定义实例方法，格式化打印实例属性name的值
    def speak(self):
        print(f'hello! 我是{self.name}')
# 自定义实例方法，占位作用
    def relation(self):
        pass
 
class Student(Person):
# 重写实例对象的构造（初始化）方法，并调用父类实例属性的赋值
    def __init__(self,name,gender,score,major,__stu_num='2018014002'):
        super(Student, self).__init__(name,gender)
        self.score = score
        self.major = major
        self.__stu_num = __stu_num
# 自定义实例方法，格式化打印实例属性stu_num的
    def speak(self):
        print(f'hi,我是{self.name}\n我的学号为{self.__stu_num},很高兴认识大家')
# 自定义实例方法，判断学号是否为既定值，并根据进行分类打印
    def identify_stu(self):
        if self.__stu_num == '2018014002':
            print('我的分组已经完成')
        else:
            print('请稍后，马上为你自动分组')
# 自定义实例方法，设置实例对象的学号为传入的值
    def set_num(self,new_num):
        self.__stu_num = new_num
# 自定义实例方法，判断该类是否为Person类的子类
    def relation(self):
        result = issubclass(Student,Person)
        if result:
            print('我的父类是Person')
        else:
            print('父类正在查询中')
            

if __name__ == '__main__':
    stu = Student('小明', '男', 90, '数学')
 # 调用speak方法 打印stu对应的值
    stu.speak()
 # 调用实例方法 鉴别学号是否为指定值
    stu.identify_stu()
 # 调用实例方法 鉴别实例对象所属的类的父类是否为
    stu.relation()
    print("******************")
    stu_2 = Student('小红', '女', 89, '英语')
 # 调用实例方法 设置stu_2的学号为'2018040625'
    stu_2.set_num('2018040625')
 # 调用实例方法 打印stu_2对应的值
    stu_2.speak()
 # 调用实例方法 鉴别学号是否为指定值
    stu_2.identify_stu()
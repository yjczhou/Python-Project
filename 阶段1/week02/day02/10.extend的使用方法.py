# coding:utf-8

# 将其他列表或元组中的 元素 导入 到 当前列表或元组中
# list.extend(iterable)  iterable代表列表或元组

# 导入列表
students = ['dewei','xiaomu','xiaogang']
new_students = ['xiaowang','xiaohong']
students.extend(new_students)
# students += new_students
print(students)

# 导入元组
history = []
new_history = ('zhonguo','meiguo')
history.extend(new_history)
print(history)

# 导入字符串
test =[]
test.extend('abcdf') #会把字符串分割
print(test)
# test.extend(1)
# 报错不能是整型 None bool
# 如果是字典，则只能得到key
print(test)
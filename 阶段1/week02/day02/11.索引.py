# coding:utf-8

# 字符串，列表和元组都有索引
# 从最左边记录的位置就是索引
# 索引用数字表示，起始从0开始
# 字符串，列表（元组）的最大索引是他们的长度-1
# 不能超出索引会报错
I = ['name']
print(I[0])

# 索引用来对单个元素进行访问，切片则对一定范围内的元素进行访问
# 切片通过冒号在中括号内把相隔的两个索引查找出来 [0:10]
# 切片规则：左边包含，右边不包含
# 通过切片生成不是原有的
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[3:8]) #[4, 5, 6, 7, 8]
# 获取列表完整数据
# 左边不写默认为0，右边默认为最大
print('获取列表完整数据',numbers[:])
print('另一种获取完整列表的方法',numbers[0:])
# 负数是从右边向左边数 ，最右边是-1
print('获取列表的方法',numbers[0:-1])
# 列表的反序
print('列表的反序',numbers[::-1])
# 列表的反项获取
print('列表的反向获取',numbers[-3:-1])
# 通过步长取值
print('通过步长取值',numbers[0:8:2])
# 切片生成空列表
print('切片生成空列表',numbers[0:0])


# 列表的所有，获取与修改
# list[index] = new_item
# 数据的修改只能在存在的所有范围内
tests = ['a','b','c']
tests[2] = 's'
print(tests)
# 两种写法都行
numbers[2:5] = 'a','b','c'
numbers[2:5] = ['a','b','c']
print(numbers)
# tests[3] = '0' # 报错 超出索引
# 列表无法通过添加新的索引的方式赋值
# list.index(item) # 查找对应元素的索引值
print(numbers.index('c'))

# pop函数
# 通过索引删除并获取列表的元素
# pop_item = list.pop(index)  index: 删除列表的第几个索引
# 函数会删除改索引的元素并返回
# 如果传入的index索引不存在则报错
names = ['dewei','xiaomu','xiaoguang']
pop_item = names.pop(0)
print('被删除的元素为',pop_item)
print('删除后的数组为',names)

# 通过del 删除索引
# del list[index]
# 直接删除 无返回值
# 如果index的索引不存在则报错
del names[1]
print(names)

# 索引切片在元组中的特殊性
# 可以和列表一样获取索引与切片索引
# 元组函数index和列表用法完全一致
# 无法通过索引修改与删除元素

tuple_test = (1,2,3)
del tuple_test[0] # 报错，因为元组是不可改变的


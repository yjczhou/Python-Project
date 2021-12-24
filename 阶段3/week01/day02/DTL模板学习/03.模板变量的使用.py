# coding:utf-8

# ** 掌握模板语法
# ** 掌握Python中简单数据类型的渲染
# ** 掌握Python中复杂数据类型的渲染
# ** 掌握DTL与Jinja2的使用区别

'''渲染Python中的变量'''
# 语法
    #{{value}}
# 当模板引擎遇到一个变量，它将计算这个变量，然后用结果替换它本身
# 变量名称中不能有空格或标点符号，不能以"_"开头

'''渲染静态图片'''
# 图片地址的变量
#     img_url = '/media/images/doc.jpg'
# 模板文件中渲染
#     <img src ='{{ img_url }}'>

'''渲染python中的对象'''
# 语法
    #{{object.attribute}}
# dict类型数据的渲染
# list/tuple类型数据的渲染
# list/tuple嵌套dict复杂类型数据的渲染


'''DTL与Jinja2的使用区别'''
# 注意：变量名称中不能有空格或标点符号
# 下面的语法在DTL中不被支持
    #{{object['a.b']}}
    #{{object["a b"]}}

# 类中成员的方法调用不需要(),也不支持参数传递
    #class A():
    #    def display():
    #        return 'hello'

    #a = A()
    #{{a.display}}


'''小结'''
# 记住{{variable}} 语法和variable的命名
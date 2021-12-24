# coding:utf-8

# ? 使用变量时有哪些不方便的地方？
# list/tuple如果没有循环标签，肯定很难办
# 如果能加上if、等条件判断就好了
# 页面较多，如果能共用部分页面就好了

'''模板标签的使用'''
# 语法
#     {% tag %}

'''常用的模板标签'''
# 循环控制
# 条件控制
# 模板注释
# url解析
# with语句块
# 当前时间显示
# 继承与包含

'''循环控制'''
# 语法参考
    # {% for item in data_list %}
    # <li>内容</li>
    # {% empty %}
    # <li>暂无内容</li>
    # {% endfor %}
    # # empty表示循环没有数据就展示空数据
# 循环内的变量forloop
    # 变量                  描述
    # forloop.first       如果是第一次迭代，为True
    # forloop.last        如果是最后一次迭代，为True
    # forloop.counter0    计数器，从0开始
    # forloop.counter     计数器，从1开始
# for循环dict
    # {% for key,value in data.items %}
    #     {{ key }}: {{ value }}
    # {% endfor %}
# 重复循环（循环中再循环）
    # {% cycle 'row1' 'row2' %}

'''与Jinja2的区别'''
# 循环变量forloop，Jinja2中为loop
# list为空：{% empty %}，jinja2中为{% else %}
# 循环中的再循环
#     DTL：{% cycle 'odd' 'even'}
#     Jinja2:{{ loop.cycle('odd','even')}}
# DTL 不支持continue和break

'''条件控制'''
# 语法参考
    # {% if condition_a %}
    #     满足条件a
    # {% elif condition_b %}
    #     满足条件b
    # {% else %}
    #     都不满足
    # {% endif %}
# ifequal/ifnotequal
    # {% ifequal a b %}
    # ...
    # {% endifequal %}
# 循环体内ifchanged
# 其他逻辑控制
    # and,or
    # ==,!=
    # >,<
    # >=,<=
    # in,not in
    # is


'''模板的注释'''
# 添加注释
    #{# 注释内容 #}

    # {% comment '简单的描述' %}
    #     <p>Html内容{{create_date}}</p>
    # {% endcomment %}

# 与html注释的区别
    # <!--注释的内容-->

'''url解析'''
# url标签的使用
    # {% url 'url_name' params %}
# static静态文件的解析
#     {% load static %}
#     <img src ='{% static "images/1.jpg" %}'>

'''与Jinja2的区别'''
# DTL
    # {% url 'url_name' params %}
# Jinja2
    # {{ url_for('index') }}

'''with语句块'''
# 实现块级作用域
# {% with alpha = 1 beta = 2 %}
# ...
# {% endwith %}

'''当前时间的显示'''
# {% now 'jS F Y H:i' %}
# https://docs.djangoproject.com/zh-hans/4.0/ref/templates/builtins/#std:templatefilter-date

'''DTL与Jinja2的使用区别'''
# 区别1：循环中的区别
# 区别2：url解析的区别
 
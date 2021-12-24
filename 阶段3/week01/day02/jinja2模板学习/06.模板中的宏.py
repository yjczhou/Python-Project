# coding:utf-8

'''什么是宏'''
# 把常用功能抽取出来，实现可重用
# 简单理解：宏约等于函数
# 宏可以写在单独HTML文件中

'''定义宏------像书写函数一样定义宏'''
# {% macro input(name,value='',type='text',size=20) -%}
#     <input type='{{ type }}' name="{{name}}" value="{{value|e}}" size = "{{size}}">
# {% endmacro %}

'''使用宏------像调用函数一样调用'''
# <p>{{input('username')}}</p>
# <p>{{input('password',type='password')}}</p>

'''文件中宏的使用'''
# 1. 将前面定义的宏保存为forms.html
# 2. 导入：
    # {% import 'forms.html' as forms %}
    # {% from 'forms.html' import input %}
# 3. 使用：
    #<p>{{forms.input('username')}}</p>

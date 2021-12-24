# coding:utf-8

'''模板标签'''
# 语法
    # 1:
    # {% tag %}
    # 2:
    # {% tag %}
    # 内容
    # {% endtag %}
# 标签中可包含表达式，如:if条件控制

# 条件表达式
    # {% if condition_a %}
    # 满足了条件a
    # {% elif condition_b %}
    # 满足条件b
    # {% else %}
    # 都不满足
    # {% endif %}

# if标签中的is判断
    # {% if value is defined %}
    # ...
    # {% endif %}
# 内置的判断条件
    # defined/undefined     ------------变量是否已经定义
    # none                  ------------变量是否为None
    # number/string         ------------数字/字符串判断
    # even/odd              ------------奇偶判断
    # upper/lower           ------------大小写判断
# if标签中的其它逻辑控制
    # and,or
    # ==,!=
    # >,<
    # >=,<=
    # in,not in

# for循环
# <ul>
# {% for key,value in data.items() %}
#     <li class = '{{ loop.cycle('odd','even')}}'>
#     {{ key }}: {{value}}
#     </li>
# {% else %}
#     <li>暂无数据</li>
# {% endfor %}
# </ul>

# for循环体内的变量
    # 变量              描述
    # loop.index      当前循环迭代的次数（从1开始）
    # loop.index0     当前循环迭代的次数（从0开始）
    # loop.revindex   到循环结束需要迭代的次数（从1开始）
    # loop.revindex0  到玄幻结束需要迭代的此时（从0开始）
    # loop.first      如果是第一次迭代，为True
    # loop.last       如果是最后一次迭代，为True
    # loop.length     序列的长度
    # loop.cycle      在一串序列间期取值的辅助函数

# 如果要在for循环中使用continue/break怎么办
# 扩展
# jinja_env = Environment(extensions = ['jinja2.ext.loopcontrols'])
#     {% for user in users %}
#         {%- if loop.index is even %}{% continue %}{% endif %}
#         ...
#     {% endfor%}
# 还可以添加其他扩展

# 添加注释
    # 不会显示在浏览器的Html
    # {# 注释内容 #}

# 去除html中多余的空白
    # 在块开始或结束放置一个减号'-',不能有空格
    # {% for item in seq -%}
    # {{item}}
    # {%- endfor %}

# 设置变量，赋值操作
    # 先设置，后使用，可以通过import导入
    # {% set key,value = (1,2) %}

# 使用with代码块，实现块级作用域
    # {% with %}
    #     {% set value = 42 %}
    #     {{value}} 只在代码块中有效
    # {% endwith %}

# 转义显示
# 思考：如下内容如何显示
# {{}} {% %}
# {% for key,value in data.items %}
# {{key}}:"{{value}}
# {% endfor%}
# 方式一：视为字符串
{{"{{}} {% %}"}}
# 方式二：使用raw标签
# {% raw %}
#     {% for key,value in data.items %}
#     {{key}}:"{{value}}
#     {% endfor%}
# {% endraw %}
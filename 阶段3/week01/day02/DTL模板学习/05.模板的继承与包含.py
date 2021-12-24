# coding:utf-8

'''模板的抽象与继承'''
# 步骤1：将可变的部分圈出来（base.html），就是挖出坑
    # {% block sidebar %}
    #     <!--菜单栏的内容-->
    # {% endblock %}
# 步骤2:继承父模板
    # {% extends 'base.html'}
# 步骤3：填充新内容(index.html) 就是填挖好的坑
    # {% extends "base.html"%}
    # {% block sidebar %}
    #     <!--填充的新内容-->
    # {% endblock %}
# 步骤4：复用符模板的内容（可选）
    # {% extends "base.html" %}
    # {% block sidebar %}
    # {{block.super}}
    # <!--新的菜单栏的内容-->
    # {% endblock %}

'''在模板中添加公共部分'''
# 步骤1：将可变部分拆出来(footer.html),存放到一个单独的模板文件
    # <footer>这是页脚公共的部分</footer>
# 步骤2：将拆出来的部分包进来（index.html）
    # {% extends "base.html" %}
    # {% block content %}
        # <!--页面主要内容区域-->
        #{# 公用的footer #}
        # {% include "footer.html"}
    # {% endblock %}
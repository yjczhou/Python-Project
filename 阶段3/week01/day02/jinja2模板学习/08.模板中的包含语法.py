# coding:utf-8

'''包含实现'''
# 步骤1：将可变的部分拆出来（sidebar.html）
    #<div>
    #   这是右侧公共的部分
    #</div>
# 步骤2：将拆出来的部分包进来（index.html）
    #{% include "sidebar.html"}


'''include标签'''
# 示例
# ignore missing表示包含的页面sidebar.html不存在不会报错
# {% include "sidebar.html" ignore missing %}
# 把上下文对象传递到sidebar.html页面
# {% include "sidebar.html" ignore missing with context %}
# 不要把上下文对象传递到sidebar.html页面
# {% include "sidebar.html" ignore missing without context %}


'''代码复用'''
# 当前页面的代码复用
    # <title>{% block title %}{% endblock %}</title>
    # <h1>{{self.title}}</h1>
    # {% block content %}
    # {% endblock %}


'''继承与包含区别'''
# 相关模板标签
    # {% block sidebar %}{% endblock %}          -------命名代码块
    # {% extends "base.html" %}                  -------继承模板
    # {% include "header.html" %}                -------包含代码块
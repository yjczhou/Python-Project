# coding:utf-8

'''模板过滤器'''

'''什么是过滤器'''
# 过滤器语法
    # {{value|filter_name:params}}
# 实例
    # {{value|upper}}


'''内置的过滤器'''
# 默认值显示
    # # 前面的值为False则显示默认值
    # {{value|default:''}}
    # # 前面的值如果是None的话就显示默认值
    # {{value|default_if_none:"无"}}
# 数字的四舍五入显示，后面的参数为保留几位小数
    #{{value|floatformat: 3}}
# 日期对象格式化
    #{{value|date:'D d M Y'}}
    # https://docs.djangoproject.com/zh-hans/4.0/ref/templates/builtins/#std:templatefilter-date
# 时间对象格式化
    #{{value|time:'H:i'}}
    # https://docs.djangoproject.com/zh-hans/4.0/ref/templates/builtins/#std:templatefilter-date
# 富文本内容转义显示
    #{{value|safe}}
# 字符串截取
    # {{value|truncatechars:9}}
    # {{value|truncatechars_html:9}}
    # {{value|truncatewords:2}}


'''与Jinja2的区别'''
# DTL
    #{{var|default:'我默认没有'}}
# Jinja2
    #{{var|default('我默认没有')}}
# coding:utf-8

'''自定义过滤器'''
# 步骤1：在app模块目录下新建包templatetags
    # 目录结构
    #     pools/
    #         __init__.py
    #         models.py
    #         templatetags/
    #             __init__.py
    #             poll_extras.py
    #         views.py
# 步骤2：实现过滤器poll_extras.py
    # from django import template
    # register = template.Library()
    #
    # def warning(value):
    #     """将第一个字符变红"""
    #     return '<span class="red">'+value[0]+'</span>'+value[1:]
# 步骤3：注册过滤器
    #方式1: 注册过滤器
        #register.filter('warning',warning)
    #方式2：注册过滤器
        #@register.filter(name='warning')
        #def warning(value):
            #pass

# 步骤4：在模板中使用过滤器
    #{% load poll——extras %}
    #{{value|warning}}
# ! 注意添加自定义过滤器后记得重启开发服务器
# ! 模块需要添加岛settings.py中的INSTALL_APPS内
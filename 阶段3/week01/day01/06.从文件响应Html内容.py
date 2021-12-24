# coding:utf-8

'''原理解析'''
# 1.从磁盘中读取HTML文件
# 2.替换HTML中的特殊字符
# 3.发送给浏览器


'''render_to_string()函数'''
# render_to_string(template_name,context = None,request = None,using = None)
# template_name: 模板名称
# request：请求对象
# context：模板上下文对象(dict)
# using: 模板引擎（如：Jinja2）

'''render()函数'''
# render(request,template_name,context=None,content_type = None,status = None,using=None)

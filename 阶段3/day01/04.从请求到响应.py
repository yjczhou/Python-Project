# coding:utf-8

'''什么是视图'''
# 一个视图函数，简称视图，是一个简单的python函数
# def view_name() 定义视图函数
# 例如hello模块中views.py里面的hello_world函数
# def hello_word(request):
#   return HttpResponse('hello world')
# 作用：
# 接受一个请求，返回一个响应


'''url的设计'''
# 设计简单优雅的URL
#   使用正则表达式
#   指定参数类型
# 在urls.py中练习

'''url常用配置'''
# path(route,view,name,**kwargs)函数
# route ：url匹配规则
# view ：视图函数
# name ：路由的名称
# **kwargs：其他参数
# path('hello/',hello_word)


'''include()参数解释'''
# 模块化调用
# 整合根路径与子路径
# 相当于在根路径下绑定子路径
# urls: URL匹配规则列表
# namespace：命名空间


'''url与视图的关系'''
# url的正向解析
#   url                                        视图函数
# /hello          ----------->               hello_world
#                  解析url规则

# url的逆向解析
#   url                                        视图函数
# /hello          <-----------               hello_world
#                   视图名+参数



'''视图响应的内容'''
# 响应可以是 文本，html内容，图像，甚至是404、重定向等

'''小结'''
# 视图是一个python函数，用来处理http请求
# 通过path和include配置，将url和视图函数关系建立起来
# coding:utf-8

# **思考
# ? 如何获取请求中的参数?
# ? 如何响应Html内容?

'''响应html内容'''
# def view_name() 定义视图
# from django.http import HttpResponse

# def current_datetime(request):
#     html='<html><body style="color:#f00">hello world.</body></html>'
#     return HttpResponse(html)


'''获取url的参数'''
# 获取url指定类型的参数
    # url规则：
    # path('article/<int:month>',views.article,name='article_list')
    # 输入url：
    # http://127.0.0.1:8000/artivle/05/
    # 视图编写
    # def article(request,month):
    #     return HttpResponse('article:' + month)
# 获取url中正则匹配的参数
# url正则:
    # re_path(r'^article/(?P<month>0?[1-9]|1?[012])/$',views.article,name='article_list')
    # 输入URL：
    # http://127.0.0.1:8000/artivle/05/
    # 视图编写：
    # def article(request,month):
    #     return HttpResponse('article:' + month)
    

'''获取get参数'''
# 获取请求中的(Get/Post)参数
# 输入URL：
# http://127.0.0.1:8000/search/?name=五月天
# 视图编写：
# def search(request):
#     name = request.GET.get('name',None)
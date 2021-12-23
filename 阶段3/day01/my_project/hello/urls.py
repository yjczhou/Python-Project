# coding:utf-8

# 自己新建的文件


from django.urls.conf import path, re_path
from hello.views import hello_word,hello_china,hello_html,article_list,\
                        search,render_str,render_html,http_request,http_response,\
                        http_json,http_file,no_data_404,article_detail,index,HomeView


urlpatterns = [
    path('world/',hello_word,name='hello_word'),
    path('china/',hello_china,name='hello_china'),
    # 固定的类型，字符串
    # /hello
    # 指定参数类型
    # /article/<int>
    # /article/50002
    # 使用正则表达式
    
    # 响应html内容
    path('html/',hello_html,name='hello_html'),
    

    # 获取url指定类型参数
    # path('article/<int:month>/',article_list,name='article_list'),
    
    # 获取url中正则匹配的参数
    # 字符串前面加r，表示不要转义字符串
    # ?P<month>表示命名捕获组
    # 0?表示0匹配0或1次，1?表示1匹配0次或1次
    re_path(r'^article/(?P<month>0?[1-9]|1?[012])/$',article_list,name='article_list'),
    # 这样我们就不能访问超出范围的页面
    
    
    # 获取get请求参数
    path('search/',search,name='search'),

    # 从文件响应html内容
    # 可以把模板放在子模块中
    # 不过要在settings.py的INSTALLED_APPS里面设置
    # 下面例子中，第2个子模块是渲染的子模块里面的模板
    # 使用render_to_string()
    path('render/str/',render_str,name='render_str'),
    # 使用render()
    # 可以把模板放在子模块中
    path('render/html/',render_html,name='render_html'),

    # 请求对象HttpRequest
    path('http/req/',http_request,name='http_request'),

    # 响应对象练习
    path('http/res',http_response,name='http_response'),
    path('http/json',http_json,name='http_json'),
    path('http/file',http_file,name='http_file'),

    # 视图的快捷方法
    path('404/',no_data_404,name='no_data_404'),
    path('article/<int:article_id>/',article_detail,name='article_detail'),

    # 使用函数的方式
    path('index/',index,name='index'),
    # 使用class的方式
    path('home/',HomeView.as_view(),name='home'),
]
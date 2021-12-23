"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from .my_project import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path

from django.views.static import serve
from 阶段3.day01.my_project.my_project import settings
# 整个django项目的根url
urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    # 把根路径与子路径整合在一起
    # include('hello.urls')子模块下的路径
    path('hello/',include('hello.urls'))
    # 固定的类型，字符串
    # /hello
    # 指定参数类型
    # /article/<int>
    # /article/50002
    # 使用正则表达式
]

# 重写错误的内置视图处理
handler500 = 'my_project.views.page_500'

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^public/(?P<path>.*)$',serve,{
            'document_root': settings.MEDIA_ROOT
        })
    ]

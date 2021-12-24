# coding:utf-8

# 自己新建的文件


from django.urls.conf import path, re_path
from hello.views import index,tag,test_filter,mine_filter

urlpatterns = [
    # 使用函数的方式
    path('index/', index, name='index'),
    path('tag/',tag,name='tag'),
    path('test/filter/',test_filter,name='test_filter'),
    path('mine/filter/',mine_filter,name='mine_filter'),
]
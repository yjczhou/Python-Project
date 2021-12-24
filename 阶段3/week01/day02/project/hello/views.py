import datetime

from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse, JsonResponse, FileResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView

from 阶段3.day01.my_project.my_project import settings


# Create your views here.

class Cat(object):
    def display(self):
        return '我是猫'


# ** 因为我们这里配置了jinja2模版引擎，这里如果找不到自带的模板引擎文件，会加载jinja2模板引擎文件
# ** 但是子模块下能找到自带的模本文件的话，就不会用jinja2的文件
# 使用函数的方式
def index(request):
    username = '张三'
    age = 25
    img_url = '/public/images/1.jpg'
    list_user = [
        {
            "name": '张三',
            'age':34
        },
        {
            "name": '李四',
            'age': 20
        }
    ]
    user_obj = {
        'user name':'王五',
        'user.name':'王二'
    }
    cat = Cat()
    return render(request,'index.html',{
        "username":username,
        'age':age,
        'img_url':img_url,
        'list_user':list_user,
        'user_obj':user_obj,
        'cat':cat
    })

def tag(request):
    '''DTl的标签练习'''
    list_user = [
        { "name": '张三','age': 34 },
        { "name": '李四','age': 20,'sex':'男'},
        {"name": '王五', 'age': 34},
        {"name": '李六', 'age': 20},
    ]
    # list_user = []
    return render(request,'tag.html',{
        'list_user':list_user
    })

def test_filter(request):
    """
    过滤器的使用
    :param request:
    :return:
    """
    name = 'model'
    list_user = []
    user_info = None
    pi = 3.1415926
    # 2050年9月28日
    my_date = datetime.datetime(2050,9,28)
    html = '<h3>欢迎大家学习我们的python课程，祝大家学习愉快<h3>'
    return render(request,'test_filter.html',{
        'name':name,
        'list_user':list_user,
        'user_info':user_info,
        'pi':pi,
        'my_date':my_date,
        'html':html
    })

def mine_filter(request):
    """
    自定义过滤器
    :param request:
    :return:
    """
    name = "周俊杰"
    return render(request,'mine_filter.html',{
        'name':name
    })
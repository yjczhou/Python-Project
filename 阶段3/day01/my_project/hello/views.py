from django.http.response import HttpResponse, JsonResponse, FileResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView

from 阶段3.day01.my_project.my_project import settings


# Create your views here.

def hello_word(request):
    # url逆向解析 通过函数名找到url # /hello/world/
    print(reverse('hello_word'))

    return HttpResponse('hello world')


def hello_china(request):
    # 500测试
    raise
    #
    return HttpResponse('hello china')


# 响应html内容
def hello_html(request):
    html = '<html><body style="color:#f00">hello world.</body></html>'
    return HttpResponse(html)


# 获取url参数
def article_list(request, month):
    """ 
    :param month: 今年某一个月的文章
    """
    return HttpResponse("article:{}".format(month))


# 获取get请求参数
def search(request):
    """ 
    GET参数的获取
    """
    # 获取name参数，表示没有的或给一个空值
    name = request.GET.get('name', '')
    print('参数:', name)
    return HttpResponse('查询成功')


def render_str(request):
    # render_to_string()的使用
    # 相对Templates的路径
    templ_name = 'index.html'
    # 还需要在settings.py里面修改告诉模板在哪里
    html = render_to_string(template_name=templ_name)
    return HttpResponse(html)


def render_html(request):
    # render()函数的使用
    # 相对Templates的路径
    # 同时我们可以直接在子模块中建立模板
    templ_name = 'hello/index.html'
    return render(request, template_name=templ_name)


def http_request(request):
    '''请求练习'''
    # 1.获取请求方式
    print(request.method)

    # 2.获取请求头信息
    headers = request.META
    print(headers)
    ua = headers.get('HTTP_USER_AGENT', None)
    print(ua)
    # 或者这样获取
    print(request.headers)
    print(request.headers['user-agent'])

    # 3.获取请求参数
    name = request.GET.get('name',None)
    print(name)
    return HttpResponse('响应')

# 响应练习
def http_response(request):
    # 设置响应状态码方法一
    res = HttpResponse('响应内容',status=201)
    # 设置响应状态码方法二
    res.status_code = 200
    # 查看状态码
    print(res.status_code)
    return res

def http_json(resquest):
    # 响应json
    user_info = {
        'name': '张三',
        'age': 34
    }
    return JsonResponse(user_info)

def http_file(request):
    # 响应一个文件
    # 这里的文件找的是最外层的
    response = FileResponse(open(settings.MEDIA_ROOT+'/1.jpg', 'rb'))
    return response

def no_data_404(resquest):
    # 404页面
    return HttpResponse('404')

def article_detail(request,article_id):
    """
    文章详情，ID是从1000开始的整数
    :param request:
    :param article_id:
    :return:
    """
    if article_id <1000:
        # 方式一：使用HttpResponseRedirect()
        # 这里也可以搭配逆向解析使用，更具视图函数得到页面地址，防止因为页面地址的更换，而没有修改
        # return HttpResponseRedirect(reverse('no_data_404'))
        # 方式二：使用视图快捷方式redirect()
        return redirect('no_data_404')
    return HttpResponse('文章{}的内容'.format(article_id))


# 使用函数的方式
def index(request):
    return render(request,'index.html')
# 使用class的方式
class HomeView(TemplateView):
    template_name = 'home.html'
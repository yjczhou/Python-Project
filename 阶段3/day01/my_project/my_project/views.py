# coding:utf-8
from django.http import HttpResponse


def page_500(request):
    """
    500错误页面
    :param request:
    :return:
    """
    # 我们也可以render一个界面
    return HttpResponse('服务器正忙，请稍后在试')
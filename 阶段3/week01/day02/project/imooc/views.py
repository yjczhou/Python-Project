from django.shortcuts import render


def index(request):
    """  首页 """
    return render(request, 'index.html')


def course(request):
    """  免费课程 """
    return render(request, 'course.html')


def coding(request):
    """  实战课程 """
    return render(request, 'coding.html')


def article(request):
    """  手记 """
    return render(request, 'article.html')


def wenda(request):
    """  问答 """
    return render(request, 'wenda.html')

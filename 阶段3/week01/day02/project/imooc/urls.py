from django.urls import path

from imooc import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('course/', views.course, name='course'),
    path('coding/', views.coding, name='coding'),
    path('article/', views.article, name='article'),
    path('wenda/', views.wenda, name='wenda'),
]

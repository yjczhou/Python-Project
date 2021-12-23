# coding:utf-8

'''内置序偶无处理视图'''
# 就是自带的错误图示界面
# 400 bad request
# 403 Forbidden 没有权限访问资源
# 404 not found
# 500 Internal Server Error

'''重写内置的错误处理视图'''
# 在根模块下新建views.py
# 在项目urls.py中添加配置，一般在项目最初始的urls.py里，而不是在子模块中
# handler500 = "my_project.views.page_500"
# handler400
# handler403
# handler404
# 切换到生产环境DEBUG = False


'''static.serve处理静态文件'''
# 在项目settings.py中添加配置
#   MEDIA_URL = '/public/'
#   MEDIA_ROOT = os.path.join(BASE_DIR,'public')
# 在项目urls.py中添加配置
# from django.views.static import serve
# urlpatterns = [
#     re_path(r'^public/(?P<path>.*)$',serve,{
#         'document_root':settings.MEDIA_ROOT,
#     })
# ]
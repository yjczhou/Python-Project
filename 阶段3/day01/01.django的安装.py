# coding:utf-8

'''Django的安装'''
# 方式1. pip install --trusted-host pypi.douban.com django==3.0
# 方式2. 源码安装 python setup.py install


'''检测是否安装成功'''
# import django
# django.__version__


'''django项目的创建'''
# 方式1.使用命令行生成模板
# django-admin[.py] startproject my_project
# my_project是项目名称
# 方式2.使用pycharm创建


'''django项目'''
# |--my-project                  # 项目目录
# |  |--__init__.py              # 包的入口文件
# |  |--settings.py              #项目配置文件
# |  |--urls.py                  #url访问地址配置文件   
# |  |--wsgi.py                  #部署配置
# |  |--asgi.py                  #部署配置
# |--db.sqlite3                  #sqllite数据库
# |--manage.py                   #命令行管理工具








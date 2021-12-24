# coding:utf-8

# ? 如何在django项目中使用jinja2

# ** 掌握settings.py中模板相关的配置
# ** 了解多个模板引擎支持情况下配置
# ** 掌握模板的加载顺序

'''templates相关配置'''
# 配置示例
TEMPLATES = [
    {
        # 自带的模板引擎
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 要想模板生效，我们要告诉我们的模板在哪
        'DIRS': ['templates'],
        # 设置为True表示我们可以优先去子模块下找，设置为False表示只会在templates里找HTML文件
        'APP_DIRS': True,
        'OPTIONS': {
        # 其他配置选项
        },
    }
]
'''配置选项'''
# BACKEND         -------模板引擎配置
    # django.template.backends.django.DjangoTemplates
    # django.template.backends.jinja2.Jinja2
# DIRS            -------模板引擎按列表顺序搜索这些目录以查找模板源文件
    # 推荐使用DIRS=[os.path.join(BASE_DIR,'templates')]
# APP_DIRS        -------决定模板引擎是否应该进入每个已安装的应用中查找模板
    #每种模板引擎后端都定义了一个惯用的名称作为应用内部存放模板的子目录名称
    #DTL          -------templates目录
    #Jinja2       -------jinja2目录
# OPTIONS         -------其他选项配置


'''同时支持两种模板引擎'''
# 添加配置模板引擎支持
TEMPLATES = [
    {
        # 自带的模板引擎
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 要想模板生效，我们要告诉我们的模板在哪
        'DIRS': [os.path.join(BASE_DIR,'templates')],
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        # 要想模板生效，我们要告诉我们的模板在哪
        'DIRS': [os.path.join(BASE_DIR,'jinja2')],
    }
]
# 模板引擎查找规则get_template('index.html)
    #templates/index.html
    #jinja2/index.html

'''小结'''
# 模板查找的顺序:
    #按settings.py里定义的模板引擎顺序查找，先根目录后模块目录
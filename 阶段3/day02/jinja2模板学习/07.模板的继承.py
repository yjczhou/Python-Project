# coding:utf-8

# todo:思考为什么要对模板进行抽象和维护
# todo:思考如下场景怎样设计（易维护，可扩展）
    # 每个页面都引用了公共的头部，js，css
    #有几个页面结构和内容及其相似（如：导航菜单）


'''继承实现'''
# 步骤1：将课变的部分圈出来（base.html）
    # {% block content %}
    #     <!--内容区域-->
    # {% endblock %}
# 步骤2：继承父模板
    # {% extends 'base.html' %}
# 步骤3：填充新的内容（index.html）
    # {% block content %}
    #     <!--新的内容-->
    # {% endblock %}
# 步骤4：复用符模板的内容（可选）
    # {% extends 'base.html' %}
    # {% block content %}
    #     {{super()}}
    #     <!--新的内容-->
    # {% endblock %}
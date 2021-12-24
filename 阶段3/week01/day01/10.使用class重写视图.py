# coding:utf-8

'''使用class重写视图'''
# 视图是一个可调用对象，可以接受一个请求然后返回一个响应
# 基于类的视图可以结构化你的视图
# 基于类的视图可以利用继承和混合重用代码
# 内置的视图拿来即用，代码更简洁

# 举例 TemplateView
# 步骤1: 继承视图
#   django.views.generic.TemplateView
# 步骤2: 配置模板地址
# 步骤3: 配置url

# TemplateView原理解析
# 从项目主目录寻找模板文件
# 从app的模板目录寻找模板文件

'''内置通用视图'''
# django.views.generic.ListView
# 列表类数据的封装，如：景点列表支持分页
# django.views.generic.DetailView
# 详情类数据的封装，如景点详情

'''看清视图的本质'''
# class ListView(MultipleObjectTemplateResponseMixin,BaseListView)
# 使用了多重继承


'''小结'''
# 使用class改写视图实际上是面向岁相互的改造的过程，Django内置的通用视图是代码更精简
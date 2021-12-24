# coding:utf-8

'''模板全局函数'''
# 全局函数可以在模板中使用
# 示例
# <ul>
# {% for i in range(10) %}
#     <li>{{i}}</li>
# {% endfor %}
# </ul>

'''常用全局函数'''
# range([start],stop[,step])
# dict(**items)
# cycler(**item)     ----可用于css类名的循环
# joiner(sep=',')    ----可用于字符串拼接
# url_for()          ----url解析函数（如：静态文件地址解析，链接跳转地址解析）如：url_for('static',filename='style.css'),
#                           url_for('index')，index是函数名


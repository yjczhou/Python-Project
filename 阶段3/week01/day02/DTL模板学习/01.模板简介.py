# coding:utf-8

'''模板和模板引擎'''
# 模板具有一定格式或骨架，可以动态的生成HTML
# 模板引擎决定以何种方式组织代码
# 一个项目可以有一个或多个模板引擎  DTL   Jinja2

'''DTL介绍'''
# DTL(Django Template Language) 是django原生的模板系统
# 直到Django1.8，唯一的模板引擎支持

'''Jinja2介绍'''
# 速度更快，Python的功能齐全的开源模板引擎
# 安装
# pip install jinja2

'''渲染机制'''
# 没有模板引擎怎样在浏览器展示html
    #1.从磁盘读取html字符串
    #2.将满足特定规则的内容进行替换
    #3.发送给浏览器展示

'''django中的渲染机制'''
# 步骤1：从磁盘读取模板文件（get_template）
# 步骤2：选择合适的模板引擎（select_template）
# 步骤3：将指定内容对模板进行渲染（render）
# 步骤4：发送给浏览器显示
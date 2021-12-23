# coding:utf-8

# todo:要在如下场景给予操作提示，怎么实现？
    #用户登录成功，提示：欢迎回来
    #用户发布问题成功，提示：发帖成功


'''消息闪现'''
# 第一步：在视图中产生一个消息（提示/警告/错误）
    #flash(msg_content,msg_type)
    #msg_content: 消息内容
    #msg_type: 消息类型
# 第二步：在模板中展示消息
    #get_flashed_messages(category_filter=['error'])
    #category_filter: 对产生的消息按类别查询

    # <ul class = flashes>
    # {% for category,message in get_flashed_messages(with_categories = true) %}
    #     <li class='{{category}}'>{{message}}</li>
    # {% endfor %}
    # </ul>

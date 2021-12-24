# coding:utf-8

'''什么是过滤器'''
# 过滤器：修改变量（如：格式化显示）
# 用管道符号(|)分割 如：{{name|striptags}}
# 可以链式调用 {{name|striptags|title}}
# 可以用圆括号传递可选参数{{list|join(',')}}

'''过滤器的使用'''
# 方式1：用管道符|
    # {{value|safe}}
#方式2：使用标签
# {% filter upper %}
#     this text becomes uppercase
# {% endfilter %}

'''内置过滤器'''
# 求绝对值
    # {{ value|abs }}
# 默认值显示 default(value,default_value = '',boolean = False)
    # {{ value|defalut('默认值') }}
    # {{ value|d('默认值')}} 简写
# html转义
    #{{ value | escape}}或{{value | e}}
    # 注意一般会自动转义，所以我们需要把autoescape设置为false
# 富文本内容转义显示（图文并茂）
    # {{value|safe}}
# 倒序显示
    #{{value|reverse}}


'''自定义过滤器'''
# 方式1： 使用装饰器注册
    # @app.template_filter('reverse')
    # def reverse_filter(s):
    #     return s[::-1]
# 方式2： 调用函数注册
    # def reverse_filter(s):
    #     return s[::-1]
    # app.jinja_env.filter['reverse'] = reverse_filter
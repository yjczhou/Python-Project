
# 导入包
from django import template
register = template.Library()


# 定义过滤器
# 如果我们需要传参，就在括号中加参数，例如count参数

# 使用方式二注册过滤器
@register.filter()
def fmt_uname(value,count=1):
    """
    格式化用户的昵称
    count默认等于1
    :param value:
    :return:
    """
    if count >len(value):
        raise IndexError('超出范围')
    name = value[:count]
    return '{}'.format(name)+'*'*(3-count)

# 使用方式一注册过滤器
# register.filter('fmt_uname',fmt_uname)


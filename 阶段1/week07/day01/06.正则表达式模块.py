# coding:utf-8

'''正则表达式模块-re'''

'''findall()'''
# findall(pattern,string[,flags])
# 查找字符串中所有（非重复）出现的正则表达式模块，并返回一个匹配列表

'''search()'''
# search(pattern,string,flag=0)
# 使用课选标记搜索字符串总第一次出现的正则表达式模式。
# 如果匹配成功，则返回匹配对象；如果失败，则返回None
'''group()与groups()'''
# group(num)返回整个匹配对象，或者编号为num的特定子组
# groups():返回一个包含所有匹配子组的元组(如果没有成功匹配，则返回一个空元组)
import re
test ='hello my name is dewei'
result = re.search('hello (.*) name is (.*)',test)
print(result.groups())
print(result.group(1))
print(result.group(2))
# ('my', 'dewei')
# my
# dewei

'''split()正则替换'''
# split(pattern,string,max=0)
# 根据正则表达式的模式分割符，split函数将字符串分割为列表，
# 然后返回成功的列表，分割最多操作max次，（默认分割所有匹配成功的位置）
data = 'hello world'
# 按照非字母数字下滑线分割
print(re.split('\W',data))
# ['hello', 'world']

'''match()'''
# match(pattern,string,flags=0)
# 尝试使用带有可选的标记的正则表达式的模式来匹配字符串。
# 如果匹配成功，就返回匹配对象;如果失败，就返回None
result = re.match('hello',data)
print(result.group())
# hello

'''compile()'''
# compile(pattern,flags=0)
# 定义一个匹配规则的对象
data = 'hello my email is dewei@imooc.com i like python'
re_obj = re.compile('email is (.*?) i')
result = re_obj.findall(data)
print(result)
# ['dewei@imooc.com']

'''re的额外匹配要求
属性                    描述
re.I、re.TGNORECASE     不区分大小写的匹配
re.L、re.LOCALE         根据所使用的本地语言环境通过\w.\W,\s,\S实现匹配(unicode_python2时代，可以理解为通用模式，类似utf-8)
re.M、re.MULTILINE      ^和$分别匹配目标字符串中行的起始和结尾，而不是严格匹配整个字符串本身的起始
re.S、re.DOTALL         “.”通常匹配除了\n之外的所有单个字符；该标记表示“.”能够匹配全部字符
re.X、re.VERBOSE        忽略规则表达式中的空白和注释
'''


def check_url(url):
    re_g = re.compile('[a-zA-Z]{4,5}://\w*\.*\w+\.\w+/')
    # \.表示普通的.
    result = re_g.findall(url)
    if len(result) != 0 :
        return True
    else:
        return False
def get_url(url):
    # 我们只想要这一部分，所以可以使用组
    re_g = re.compile('[a-zA-Z]{4,5}://(\w*\.*\w+\.\w+)/')
    result = re_g.findall(url)
    if len(result)!=0:
        return result[0]
    else:
        return ''

def get_email(email):
    re_g = re.compile('[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]+')
    result = re_g.findall(email)
    return result

html = ('<div class="s-top-nav" style="display:none;">'
        '</div><div class="s-center-box"></div>')

def get_html_data(html):
    re_g = re.compile('style="(.*?)"')
    result = re_g.findall(html)
    return result  

def get_all_data(html):
    re_g = re.compile('="(.+?)"')
    result = re_g.findall(html)
    return result

if __name__ == '__main__':
    url = 'https://www.imooc.com/'
    result = check_url(url)
    print(result)
    print(get_url(url))
    
    email = 'dewei@imooc.com'
    result = get_email(email)
    print(result)
    
    print(get_html_data(html))
    
    print(get_all_data(html))
    
    # 
    re_g = re.compile(('<div class="(.*?)" style="(.*?)">'
        '</div><div class="(.*?)"></div>'))
    result = re_g.search(html)
    print(result.groups())
    
    re_g = re.compile('\s')
    result = re_g.split(html)
    print(result)

    # re_g = re.compile('class="(.*?)"')
    # match函数从头开始匹配，所以找不到class，会返回None
    re_g = re.compile('<div class="(.*?)"')
    result = re_g.match(html)
    # <re.Match object; span=(0, 22), match='<div class="s-top-nav"'>
    print(result)
    print(result.group())
    print(result.span())
    print(html[:22])
# coding:utf-8

import re


def check_url(url):
    # \.表示普通的.
    result = re.findall('[a-zA-Z]{4,5}://\w*\.*\w+\.\w+/',url)
    if len(result) != 0 :
        return True
    else:
        return False
def get_url(url):
    # 我们只想要这一部分，所以可以使用组
    result = re.findall('[a-zA-Z]{4,5}://(\w*\.*\w+\.\w+)/',url)
    if len(result)!=0:
        return result[0]
    else:
        return ''

def get_email(email):
    result = re.findall('[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]+',email)
    return result

html = ('<div class="s-top-nav" style="display:none;">'
        '</div><div class="s-center-box"></div>')

def get_html_data(html):
    result = re.findall('style="(.*?)"',html)
    return result  

def get_all_data(html):
    result = re.findall('="(.+?)"',html)
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
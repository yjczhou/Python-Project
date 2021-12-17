# coding:utf-8

def login(username, password):
    if username=='mooc' and password == '123456':
        print('登录成功')
    else:
        print('请重新登录')

login('mooc','12345')
# coding:utf-8

'''请求对象HttpRequest'''
# 请求方式method（POST/GET）
# 请求头信息META/headers
#       REMOTE_ADDR --- 请求的ip地址
#       HTTP_USER_AGENT --- 用户请求终端信息
# 获取请求传递参数
#       GET   --- GET请求参数
#       POST  --- POST请求参数
#       Cookies -- cookies信息
#       files --   文件信息


'''响应对象'''
# HttpResponse
# HttpResponseRedirect--重定向
# JsonResponse -- 响应json
# FileResponse --响应文件
# 关系
#                                    HttpResponseBase
#                                   |                |
#                          HttpResponse         StreamingHttpResponse
#                              |                                |
#                          JsonResponse                    FileResponse

'''HttpResponse'''
# status设置HTTP响应状态码
# status_code 查看Http响应状态码
# content-type 设置响应的类型
# write() 写入响应内容

'''JsonResponse'''
# 示例
# from django.http import JsonResponse
# response = JsonResponse({
#     'username':'admin',
#     'passwd':'123456',
#     'sex':'男'
# })

'''FileResponse'''
# from django.http import FileResponse
# response = FileResponse(open('myfile.png','rb'))

'''常见的Content-Type'''
# text/html 超文本标记语言文本（html）
# text/plain 普通文本
# text/xml xml文档
# image/png、image/jpeg、image/gif  图片或图形
# application/json  json数据类型
# coding:utf-8

# isspace 判断字符串是否是一个由 空格 组成的字符串
# booltype = string.isspace() 无参数可传，返回一个布尔类型
print(' '.isspace(),'hello xiaomu'.isspace())
# 注意由空格组成的字符串，不是空字符串


# istitle 判断字符串是否是一个标题类型
# 一个字符串有多个单词，每个单词首字母都是大写，其余字母小写  这就是标题
# booltype = string.istitle() 无参数可传，返回一个布尔类型
print('Hello Xiaomu'.istitle(),'hello xiaomu'.istitle())
# 该函数只用于英文

# isupper判断字符串中的字母是否都是大写
# islower判断字符串中的字母是否都是小写
# booltype = string.isupper() 无参数可传，返回一个布尔类型
# booltype = string.islower() 无参数可传，返回一个布尔类型
print('hello xiaomu'.isupper(),'hello xiaomu'.islower())
# 只检查字符串中的字母，对其他字符不做判断
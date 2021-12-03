# coding:utf-8

# strip 将去掉字符串左右两边的指定元素，默认是空格
# 'string'.lstrip() 去除左边
# 'string'.rstrip() 去除右边
# newstr = string.strip(item) item: 你想去掉的元素，不填写则去掉空格

# 传入的元素如果不在开头或结尾则无效

name = '   nihao   '
name1 = 'nihaoin'
print(name)
print(name.strip())
print(name1.strip('n'))
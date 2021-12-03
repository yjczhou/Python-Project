# coding:utf-8

# 为字符串定义长度，如不满足，缺少的部分用0在左边补齐
# newstr = str.zfill(width)  width:新字符串希望的宽度
# 注意事项
# 与字符串的字符无关
# 如果定义长度小于当前字符串长度，则不会发生变化


name = 'xiaomu'
new_name = name.zfill(10);
print(new_name) #0000xiaomu

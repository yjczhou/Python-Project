# coding:utf-8

# 将字符串的首字母大写，其他字母小写

# 用法: newStr = string.capitalize()
# 注意事项：
# 只对第一个字母有效
# 只对字符串中字母有效
# 已经是大写则无效
info = 'hello 小慕'
name = 'xiaoMu'
new_name = name.capitalize()
new_info = info.capitalize()
print(new_info) #Hello 小慕
print(new_name) #Xiaomu
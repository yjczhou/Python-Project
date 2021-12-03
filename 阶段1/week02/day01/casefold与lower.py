# coding:utf-8

# 将字符串全体小写
# newstr = str.casefold()
# newstr = str.lower()
# 注意事项
# 只对字符串中的字母有效
# 已经是小写，则无效
# lower只能对英文进行小写，而casefold可以对更多语种小写
name = 'DEWEI 你好'
new_name1 = name.casefold();
new_name2 = name.lower();

print(new_name1,new_name2) #dewei 你好 dewei 你好
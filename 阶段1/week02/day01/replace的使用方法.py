# coding:utf-8

# 将字符串中old（旧元素）替换成new（新元素），并能指定替换的数量
# newstr = string.replace(old,new,max)
# old: 被替换元素 new: 新元素 max: 可选参数，代表替换几个，默认全部替换全部匹配的old元素

print('hello dewei'.replace('dewei','xiaomu'))
print('hello xiaomu'.replace('l','0',1))

# 代表一个字符串
info = ('lorem saeknfuierwafhni eu'
        'lorem saeknfuierwafhni eu'
        'lorem saeknfuierwafhni eu'
        'lorem saeknfuierwafhni eu'
        'lorem saeknfuierwafhni eu')

# replace()还可以链式操作
print('hello dewei'.replace('e','a').replace('a','e'))
# coding:utf-8

# for循环中的for循环
a = [1,2,3]
b = [4,5,6]
for i in a:
    for j in b:
        print(i+j,end='')
    print('\n')
# coding:utf-8

# 计算1到100以内能被3或者7整除，但不能
# 同时被3和7整除的数的个数，运行结果为
# 39
count = 0
for i in range(1,101):
    if (i%3==0 or i%7==0) and not (i%3==0 and i%7==0):
        count += 1
print(count)

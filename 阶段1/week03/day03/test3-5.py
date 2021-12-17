list = [1,2,3,4,5,6,7,8,9,10]
count = 1
for i in list:
    if i%2 == 0:
        print(f'第{count}个偶数{i}')
        count = count + 1
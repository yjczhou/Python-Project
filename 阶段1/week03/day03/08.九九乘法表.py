# coding:utf-8

for i in range(1,10):
    j = 1
    while j <= i:
        print(f'{j} * {i} = {i*j} ',end='\t')
        j = j+1
    print('')
print('-------------------------------------------------------------------------------------------------------------------------')
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j} * {i} = {i*j} ',end='\t')
    print('')
    
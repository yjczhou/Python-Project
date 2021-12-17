# coding:utf-8

str = """ 
**********欢迎使用货币住哪换服务系统**********
1.人民币转换美元
2.美元转换人民币
3.人民币转欧元
0.结束程序
"""
print(str)
number = input('请你选择需要的服务:')
if number == '0':
    print('感谢你的使用，祝你生活愉快，再见')
    exit()
elif number == '1':
    print('欢迎使用人民币转换美元服务')
    money = input('请你输入需要转换的人民币金额:')
    print(f'你需要转换的人民币为:{money}')
    new_money = (float(money)/7.06)
    new_money = round(new_money,2)
    print(f'对换成美元为{new_money}')
    print('='*23)
    exit()
elif number == '2':
    print('欢迎使用美元转换人民币服务')
    money = input('请你输入需要转换的美元金额:')
    print(f'你需要转换的美元为:{money}')
    new_money = (float(money)*7.06)
    new_money = round(new_money,2)
    print(f'对换成人民币为{new_money}$')
    print('='*23)
    exit()
elif number == '3':
    print('欢迎使用人民币转换欧元服务')
    money = input('请你输入需要转换的人民币金额:')
    print(f'你需要转换的人民币为:{money}')
    new_money = (float(money)*0.12)
    new_money = round(new_money,2)
    print(f'对换成欧元为{new_money}')
    print('='*23)
    exit()
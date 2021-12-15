# coding:utf-8

'''利用内置函数open获取文件对象'''
# 功能：生成文件对象，进行创建，读写操作
# open(path,mode)
# 参数说明：
# path：文件路径
# mode：操作模式
# 返回值：文件对象
# 例子：f = open('d://a.txt','w')   写操作

# w模式 如果文件不存在，会新创建，如果文件里面有内容会重新覆盖

'''
文件操作的模式之写入
模式        介绍
w           创建文件
w+          创建文件并读取文件
wb          二进制形式创建文件
wb+         二进制形式创建或追加内容
a           追加内容
a+          读写模式的追加
ab+         二进制形式读写追加
'''

'''
文件对象的操作方法
方法名      参数            介绍            举例
write       Message         写入信息        f.write('hello\n')
writelines  Message_list    批量写入        f.writelines(['hello\n','world\n'])
close       无              关闭并保存      f.close()
'''
# 注意：操作完成后，必须使用close方法

# windows 系统中写入中文时，需要设置编码格式，例如
# f.open(xxx+'/'+'x.txt','w',encoding='utf-8')
# 在当前目录创建一个a.txt文件
# 使用w就无法调用读的函数，但是w+可以
f  = open('a.txt','w+',encoding='utf-8')
# 向文件中书写内容
f.write('hello 小慕')
# 读取文件
# seek()从哪里开始读取
f.seek(0)
# read()默认读取最后一个
print(f.read())
#当使用w时会报 io.UnsupportedOperation: not readable
# 关闭文件对象
f.close()
print('---------------------------')
f1 = open('b.txt','ab')
message = 'python很有意思'
# 有中文不能直接转成比特类型
# 需要下面的形式
_message = message.encode('utf-8')
f1.write(_message)
f1.close()

l = ['\n今天天气很好\n','很适合学习python\n','python是非常简单的编程语言\n']
f2 = open('b.txt','a',encoding='utf-8')
f2.writelines(l)
f2.close()
# coding:utf-8

# sort函数
# 对当前列表按照一定规律进行排序
# list.sort(key=None,reverse=False)
# key 参数比较
# reverse 排序规则，reversr = True 降序 ; reverse = False 升序 （默认）

# 列表中元素类型必须相同，否则无法排序报错

books = ['python','django','web','flask','tornado']
# 按照字母顺序排列
books.sort()
print(books)

books.sort(reverse=True)
print(books)
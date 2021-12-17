# coding:utf-8

class ShortInputException(Exception): 
    # 自定义异常类 
    def __init__(self, length, atleast):
        self.length = length 
        self.atleast = atleast 
        
def main():
    try:
        text = "abc" 
        if len(text) < 5: 
            raise ShortInputException(len(text),5) 
    except ShortInputException as result:
        print("ShortInputException:输入的长度为: {}," "长度至少应该是：{}".format(result.length, result.atleast)) 
    else:
        print("没有异常的发生") 
    finally: print("输入的字符串是{}".format(text))   

main()
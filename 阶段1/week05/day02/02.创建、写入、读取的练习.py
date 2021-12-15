# encoding:utf-8
import os

def create_package(path):
    if os.path.exists(path):
        raise Exception('%s 已经存在不可创建' % path)
    os.makedirs(path)
    init_path = os.path.join(path,'__init__.py')
    f = open(init_path,'w')
    f.write('#coding:utf-8\n')
    f.close()


class Open(object):
    def __init__(self,path,mode = 'w',is_return =True):
        self.path =path
        self.mode = mode
        self.is_return = is_return
    
    def write(self,message):
        f = open(self.path,self.mode,encoding='utf-8')
        if self.is_return:
            if not message.endswith('\n'):
                message = '%s\n' % message
        try:
            f.write(message)
        except Exception as e:
            print(e)
        finally:
            f.close()
    def read(self,is_strip=True):
        _data = []
        # with关键字 会自动关闭文件
        with open(self.path,mode=self.mode,encoding='utf-8') as f:
            data = f.readlines()
        for item in data:
            if is_strip:
                temp = item.strip()
                if temp != '':
                    _data.append(temp)
            else:
                if item != '':
                    _data.append(item)
        print(_data)
        
if __name__ == '__main__':
    # 获得当前路径
    current_path = os.getcwd()
    # path = os.path.join(current_path,'test1')
    # create_package(path)
    
    # 使用Open类的方法
    open_path = os.path.join(current_path,'b.txt')
    # opentxt = Open(open_path)
    # opentxt.write('你好小慕')
    opentxt = Open(open_path,mode='r')
    opentxt.read()
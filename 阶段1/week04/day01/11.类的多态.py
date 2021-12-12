# coding:utf-8

'''什么是类的多态'''
# 同一个功能的多状态化

'''多态的用法'''
# 子类中重写父类的方法

# 1.书写一个父类
class XiaomuFather(object):
    def talk(self):
        print('小慕的爸爸说了一句话')

# 2.书写一个子类，并且继承一个父类
class XiaomuBrother(XiaomuFather):
    def run(self):
        print('小慕哥哥在奔跑着')
    # 重写了父类的方法
    def talk(self):
        print('小慕的哥哥说了一句话')

# 为什么要去多态
# 为什么要继承父类
# 为了使用已经写好的类中的函数
# 为了保留子类中某个和父类名称一样的函数的功能，这时候，我们就用到了类的多态。
# 可以帮助我们保留子类中的函数功能

class Xiaomu(XiaomuFather):
    def talk(self):
        print('haha 小慕也可以开心的说自己的观点')
if __name__ == '__main__':
    xiaomu_brother = XiaomuBrother()
    xiaomu_brother.run()
    xiaomu_brother.talk()
    
    xiaomu_father = XiaomuFather()
    xiaomu_father.talk()
    
    xiaomu = Xiaomu()
    xiaomu.talk()
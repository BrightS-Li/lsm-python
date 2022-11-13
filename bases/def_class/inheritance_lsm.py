# 继承

'''
为什么要使用继承？
    1.创建和现有类功能类类似的新类
    2.又或者新类只需要在现有类基础上添加一些成员(属性和方法)
    3.通过使用继承,可以轻松实现类的重复使用

子类：继承父类,拥有父类所有所有的属性和方法(包括私有的)
父类：派生子类
多继承:一般不使用,类名1和类名2重复的属性和方法
        先调用类名1(按顺序来)
class 类名(类名1,类名2)
    # 类定义部分
'''

class Demo_1:
    def draw(self,s):
        return s
class Demo_2(Demo_1):
    def area(self,t):
        return t
a = Demo_2()
print(f'\n---这是父类---\n{a.draw("JQK")}')
print(f'\n---这是子类---\n{a.area("AQK")}')

class People:
    def say(self):
        return self.name
    def fly(self):
        print(f'\n---这是父类中的fly---')
class Animal:
    def display(self):
        print('人也是高级动物')
class Person(People,Animal):
    def fly(self):
        '''
        重写父类中的fly
        '''
        print(f'\n---这是子类中的fly---')

b = Person()
b.name = 'lsm'
print(f'\n---这是父类---\n{b.say()}')
b.display()
# 重写
b.fly()
# 调用父类中的fly,未绑定的方法
People.fly(b)
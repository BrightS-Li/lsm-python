# super()

'''
如果子类继承多个父类，父类中存在多个同名的类实例方法(构造方法也算)

'''
class Demo_1:
    def __init__(self,name):
        self.name = name
    def say(self):
        return self.name
class Demo_2:
    def __init__(self,food):
        self.food = food
    def display(self):
        return self.food
class zilei(Demo_1,Demo_2):
    pass

a = zilei('lsm')
print(f'\n---这是Demo_1中say---\n{a.say()}')
print(f'\n---这是Demo_2中say---\na.display()报错,lsm参数传给了第一个父类,没有food参数')

# 需要重写父类的构造方法
# 在子类中定义构造方法，必须在该方法中调用父类的构造方法
'''在子类中调用父类的构造方法
使用super()函数
'''
class Demo_3(Demo_1,Demo_2):
    # 自定义构造方法
    def __init__(self,name,food):
        # 使用super调用
        super().__init__(name)
        Demo_2.__init__(self,food)
        
        # # 使用类名.__init__(self.xxx)调用多个父类
        # Demo_1.__init__(self,name)
        # Demo_2.__init__(self,food)


s = Demo_3('lsm','foodd')
print(f'\n---这是Demo_1中say---\n{s.say()}')
print(f'\n---这是Demo_2中say---\n{s.display()}')


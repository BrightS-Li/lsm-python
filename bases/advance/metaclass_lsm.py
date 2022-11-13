# metaclass 元类
'''
格式：
    1.必须继承type类
    2.需要定义并实现__new__()方法，并返回该类的一个实例对象

'''
class Demo(type):
    def __new__(cls,name,bases,attrs):
        '''
        cls代表动态修改的类
        name代表动态需改的类名
        bases代表动态被修改的类的所有父类
        attr代表被动态修改的类的所有属性,方法组成的字典
        '''
        attrs['name'] = 'lsm'
        attrs['say'] = lambda self:print('say方法')
        return super().__new__(cls,name,bases,attrs)
    
# 元类中手动添加了一个name属性，和say方法
# 通过Demo添加创建的类，会额外添加name和say方法
# 创建该类时，元类中__new__方法就会被调用，从而实现动态修改类属性或类方法的目的
class Demo_1(object,metaclass=Demo):
    pass

s = Demo_1()
print(s.name)
s.say()
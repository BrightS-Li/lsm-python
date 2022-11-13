# __slots__
'''
1.限制类实例动态添加属性和方法(__slots__是一个元组)
2.只有在__slots__定义中,才嫩被添加
3.__slots__子类不会被继承
4.子类会继承父类的__slots__,范围自身__slots__+ 父类的__slots__

类属性和slots不能同名
'''
class Demo:
    __slots__= ('name','add')


a = Demo()
a.name = 'lsm' 
print(f'\n---添加name属性---\n{a.name}')

# 限制实例对象动态添加，但是可以类添加
def info(slef):
    return '类.方法添加【限制的是实例对象】'
Demo.say = info
b = Demo()
print(f'\n---添加类say方法---\n{b.say()}')
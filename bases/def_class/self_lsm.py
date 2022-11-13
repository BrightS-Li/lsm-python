# 变量，self

'''
:类变量(类属性):        1.类体中，所有函数之外，定义的变量
                       2.所有实例化对象共享，更改一个即所有更改
:实例变量(实例属性):    1.类体中,函数内,self.变量名 ,
                      2.只作用与调用方法的对象，只能通过对象名访问,
                      3.需要先调用方法
                      4.更改实例变量，不会更改其他实例化对象
:局部变量：            1.函数内部，变量名=变量值
                      2.只能用于所在函数中
                      3.函数执行完成后，局部变量也会销毁
'''
'''
:self: 构造方法,实例方法最少有一个参数self
       slef相当于c++,this指针
       a = Demo_1()  self相当于a
       b = Demo_1()  self相当于b
---创建对象或者实例化(开辟空间),空间就时self,创建时a,b就是空间名字
'''
print('--------------------Demo------------------------')
class Demo:
    # 类变量(类属性)
    name = 'li'

    # 类方法（实例方法）
    def print_lsm(self):
        # 实例变量
        self.s = '这就是实例变量'

# 调用类变量
x = Demo()
print(Demo.name,x.name)
x.print_lsm()
print(x.s)

print('--------------------Demo_1------------------------')
class Demo_1:
    '''没有其他参数的__init__()'''

    # 类变量
    name = 'li'

    # 构造方法（特殊的类实例方法）
    def __init__(self):
        print('\n----仅有self的__init__()----')
        print('1.仅有self的__init__()又被称为默认构造方法（也叫特殊的实例方法）')
        print('2.a = Demo_1()创建了一个名为a的Demo_1类对象')
        print('3.没有__init__()或仅有self,则创建类对象时的参数可以不写,如:a=Demo_1()')
        print('4.创建a这个对象时,隐士的调用了__init__()构造方法')

    # 类方法（实例方法）
    def print_lsm(self):
        self.s = '--> 实例变量s   [必须先调用方法，这就是实例变量]'

#直接调用，自动我们手动创建的__init__()构造方法
a = Demo_1()
b = Demo_1()

# 调用类变量，类名.类变量，类对象.类变量
print('\n----调用·类变量----')
print(f'\n1.类名.类变量-\n{Demo_1.name}',f'\n-类对象.类变量-\n{a.name}')
Demo_1.name = '.类变量-调用更改'
print(f'\n2.类名更改类变量-\n类名{Demo_1.name}\n类对象{a.name}')

# 调用实例变量， 必须 对象名.实例变量【需要手动调用方法】
print('\n----调用·实例变量----')
a.print_lsm()
print(f'\n1.对象名.实例变量---\n{a.s}')
a.s = '通过对象名修改实例变量(对象名.实例变量),不会更改其他对象的实例变量'
b.print_lsm()
print('\n2.更改实例变量,不会影响类的其他实例化对象---')
print(f'.这是更改后的a对象的{a.s}')
print(f'.这是更改后的b对象的{b.s}')



print('--------------------Demo_2------------------------')
class Demo_2:
    '''有其他参数的__init__()'''

    # 类变量(类属性)
    name = 'li'
    age = 1

    def __init__(self,name,age):
        # 实例变量
        self.name = name
        self.age = age
        print('\n----有其他参数的__init__()----')
        print('..存在其他没有设置默认参数，则创建类对象时必须传入参数,如:a=Demo_2("ming",1)')
        print(f'name:{name}\nage:{age}')

    # 类方法（实例方法）
    def print_lsm(self):
        self.s = '这就是实例变量'

b = Demo_2('ming',1)



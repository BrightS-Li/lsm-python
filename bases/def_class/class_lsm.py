# 类方法，实例方法，静态方法
'''
: 实例方法:     1.第一个参数self,
               2.只能由'实例对象'访问【类名访问时,手动传入slef的实例对象】
               3.只能访问实例属性,self.变量名
: 类方法：   1.第一个参数cls,
            2.@classmethod装饰器
            3.实例对象和类对象都能访问
            4.传递类变量（类属性）
: 静态方法：   1.参数随意,但没有'self,cls'
              2.@staticmethod装饰器
              3.不能访问类的属性和方法,【类名.变量名不推荐】
调用方法括号:加括号,调用的是函数执行结果
            不加括号,调用的是整体函数，返回存储空间
'''

import time

class Demo:
    # 类属性
    name = 'li'
    age = 18
    # 构造方法，也属于实例方法
    def __init__(self,name,age):
        self.name = name # 实例属性
        self.age = age
        
    # 实例方法
    def print_lsm(self):
        s = f'\n这是实例方法--传递实例属性,name:{self.name}  age:{self.age}'
        return s
    
    # 非绑定实例方法
    def lsm(self):
        s = f'{self},手动传入slef对象'
        return s
    
    # 类方法
    @classmethod
    def info(cls):
        s = f'\n这是类方法--传递类属性,name:{cls.name}  age:{cls.age}'
        return s

    # 静态方法
    @staticmethod
    def static_method():
        s = f'\n这是静态方法--传递类属性,name:{a.name}  age:{a.age}'
        return s
    
    @staticmethod    
    def show_time():
        locl_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        return locl_time

# 实例化
a = Demo('ming',20)
# 调用实例化方法，类对象调用
print(f'\n---实例方法调用---\n-对象调用-{a.print_lsm()},\n-直接调用(传入self实例)-{Demo.print_lsm(a)}')
print('#只能访问实例属性self.变量名')
# 调用类方法
print(f'\n---类方法调用---\n-对象调用-{a.info()}',f'\n-直接调用-{Demo.info()}')
print('#可以直接访问类属性cls.变量名')
# 调用静态方法
print(f'\n---静态方法调用---\n-对象调用-{a.static_method()}',f'\n-直接调用-{Demo.static_method()}')
print('#不直接访问类属性（类名.变量名不推荐）')

print(f'\n---静态方法常见写法---\n{Demo.show_time()}')
print(f'\n---非绑定方法---\n' + Demo.lsm('lsm'))
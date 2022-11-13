# property @property
'''
: 1.类对象.属性的方式访问类中的属性,欠妥
  2.类包含的属性应该是隐藏的
  3.只允许通过类提供的方法来间接实现对类属性的访问和操作
'''
# 原理（麻烦）
class Demo:
    # 构造函数
    def __init__(self,name):
        self.name = name
    # 设置name属性值的函数
    def setname(self,name):
        self.name = name
    # 访问name属性值的函数
    def getname(self):
        return self.name
    # 删除name属性值的函数
    def delname(self):
        self.name = 'xxx'

s = Demo('li')
# 获取name属性值
print(f'\n---获取name属性值---\n{s.getname()}')
# 设置name属性值
s.setname('lsm')
print(f'\n---设置name属性值---\n{s.getname()}')

# 删除name属性值
s.delname()
print(f'\n---删除name属性值---\n{s.getname()}')


print('\n===========================Demo2============================')
# 使用property()函数
# 属性值 = property(fget = None, fset = None, fdel = None,doc = None)
class Deom_2:
        # 构造函数
    def __init__(self,name):
        self.__name = name
    # 设置name属性值的函数
    def setname(self,name):
        self.__name = name
    # 访问name属性值的函数
    def getname(self):
        # 返回name属性，如果返回slef本身，又会调用getname()，所以使用私用属性__name
        return self.__name
    # 删除name属性值的函数
    def delname(self):
        self.__name = 'xxx'
    # 为name属性配置property()函数
    # 如果没有delname就表示没删除权限，name属性可读可写
    name = property(getname,setname,delname,'这里是明文档')



# 调用说明文档的两种方法
print(f'\n---调用说明文档---\n{Deom_2.name.__doc__})',help(Deom_2.name))

a = Deom_2('JQK')
# 调用getname()方法
print(f'\n---调用getname()方法---\n{a.name}')
# 设置name属性值
a.setname('lsm')
print(f'\n---设置name属性值---\n{a.getname()}')

# 删除name属性值
del a.name
print(f'\n---删除name属性值---\n{a.getname()}')

print('\n===========================Demo3============================')
# @property
class Deom_3:
    '''
    : 把类的方法伪装成属性调用的方式
      Demo.setname(),变为Demo.setname [不加括号了]
    '''
    # 构造函数
    def __init__(self,name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name
    
    @name.deleter
    def name(self):
        self.__name = 'xxx'
        

c = Deom_3('JQK')
# 调用getname()方法
print(f'\n---调用getname()方法---\n{c.name}')
# 设置name属性值
c.name = 'lsm'
print(f'\n---设置name属性值---\n{c.name}')

# 删除name属性值
del c.name
print(f'\n---删除name属性值---\n{c.name}')
# 封装

'''
1.设计类时,刻意的将一些属性隐藏在类的内部
2.无法直接以"类对象.属性名"(或"类对象.方法名(参数)")来调用
3.只能用未隐藏的类方法间接操作这些隐藏的属性和方法

为什么要封装？
1.为了保证类内部数据结构的完整性
2.可以避免一些用户对类属性或方法的不合理操作
3.提高代码的复用性

python封装:
1.默认情况下,类中变量和方法都是共有的,名称前没有_
2.名称前__开头,属性等同于private
'''
class Demo:
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        if len(name) < 3:
            print('名称必须大于3!')
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if age < 0:
            print('年龄不能小于0')
        self.__age = age

    # 定义一个私有方法
    def __display(self):
        print(self.__name,self.__age)
a = Demo()
a.name = 'ls'
print(f'\n---方法名正确,调用的是方法---\n{a.name}')
a.age = 9
print(f'\n---方法名正确,调用的是方法---\n{a.age}')
a.li = 'ms'
print(f'\n---方法名不正确，这是就是添加的类属性---\n{a.li}')
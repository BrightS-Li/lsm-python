
# property(): 
		只允许通过类提供的方法来间接实现对类属性的访问和操作
		属性值 = property(fget = None, fset = None, fdel = None,doc = None)

					
# slots：限制动态添加
							
		1.可以通过类.方法，类.变量添加
		2.不能通过实例对象添加
						
# type()：
		type(name,base,dict) 创建类

# super()

# metaclass
		class A(type):
			def __new__(cls,name,bases,attrs) ：
				return super().__new__(cls,name,bases,attrs)

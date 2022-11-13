# 描述符

'''
:一个类属性,托管给另一个类，这个属性就是一个【描述符】
· 只定义了__get__(self,obj,type=None) 非数据描述符
` 还定了__set__(self,obj,value),__delete__(self,obj) 数据描述符
'''

class Age:
    def __init__(self,value=20):
        self.value = value
    def __get__(self,obj,type=None):
        print('\n---__get__---\nobj:%s,\ntype:%s' % (obj,type))
        print('obj是Preson实例【没有实例调用,为none所以会报错】--\n',obj.name) 
        return self.value
    def __set__(self,obj,value):
        print('\n---__set__---\nobj:%s,\ntype:%s' % (obj,type))
        print('value值赋给self.value')
        self.value = value

class Preson:
    # 类属性age是一个描述符，他取决与Age类
    age = Age()

    def __init__(self,name):
        self.name = name

p1 = Preson('张三')
# 对象名.描述符，__get__被调用，参数obj是Preson实例，tpye是type(Prenson)
# 类名.描述符(Prenson.age),__get__被调用，参数obj是None，obj.name14（行）会报错
print(p1.age)

# p1.age=25 ，__set__被调用，参数obj是prenson实例，value是25
p1.age = 25
print(p1.age)
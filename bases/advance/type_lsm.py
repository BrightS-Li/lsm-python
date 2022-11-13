# type()创建类

'''
type(name,base,dict)
    name:类名
    bases:父类(元组)
    dict:属性和方法
'''

def test(self,name,age):
    return '方法'

Demo = type('Demo',(object,),{'test':test,'name':'lsm'})

s = Demo()
# 字典中test外部定义了，则是方法
print(s.test('lsm',12))

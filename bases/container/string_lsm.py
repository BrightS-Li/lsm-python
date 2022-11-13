# 字符串

name = 'hello world'
space1 = ' space '

print(name.title())  # 首字母大写
print(name.upper())  # 全部大写
print(name.lower())  # 全部小写
print('a', 'b', 'c', sep='\n')  # \n换行 \t空格
print(f'去前面空格{space1.lstrip()}ok! ,去掉前后空格{space1.strip()}ok!')

print('------------------------------------------------------------------')

# 拼接字符串

str1 = 'bob'
str2 = 'python'
str3 = 1

# +，*，逗号，%s，format，f-string
print(str1 + " " + str2 + ' ' + str(str3))  # +号拼接，bob python 1
# 赋值拼接，bob python 1（先拼接赋值，后打印print(str4)）
str4 = str1 + " " + str2 + ' ' + str(str3)
print(str1, str2)  # 逗号拼接，bob python（自动加空格，+号不加空格）
print('a-' * 5)  # *号拼接，a-a-a-a-a-
# %拼接， %d整数， %f浮点(前面数字为保留位数) 字符AA,整数000010,浮点0.770000
print('字符%s,整数%06d,浮点%03f' % ('AA', 10, 0.77))
# format拼接 python 666 format aaa
print('python {} format {}'.format(666, 'aaa'))

# join拼接字符
list1 = ['一', '二', '三', '四', '五', '六']
tuple1 = ('一', '二', '三', '四', '五', '六')
# join拼接，一二三四五六 一-二-三-四-五-六 拼接列表，元组
print(''.join(list1), '-'.join(tuple1), sep='\n')
print(f'python {str1} hello {str2}')  # f-string 拼接，直接在{}中跟变量，或者直接跟方法

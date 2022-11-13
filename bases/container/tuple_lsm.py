# 推导式
print('\n---推导式---',tuple(i for i in range(4,8)),sep='\n')

# 元组
tuple1 = ([1, 2, 3], 1, 'abc', 'o')
users = ('root', 'westos', 'redhat')
passwds = ('123', '456', '012')

# 元组内数据不可变，元组内列表数据可变
tuple1[0].append(4)
print('\n---元组内列表数据可变---', tuple1, sep='\n')  # ([1, 2, 3, 4], 1, 'abc')

# 切片
print('\n---切片---', tuple1[:1], sep='\n')

# *重复，连接
print('\n---*,+拼接---', tuple1 * 3, tuple1 + ('a', 'b'), sep='\n')

# 判断
print('\n---判断---', 'ab' in tuple1, sep='\n')

# 枚举+迭代 返回索引+value
print('\n---enumerate枚举---', list(enumerate(users)), sep='\n')
for index, user in enumerate(users):
    print(f'第{index + 1}个用户:{user}')

# 枚举+压缩
print('\n---枚举+压缩---')
for use, passwd in zip(users, passwds):
    print(user, ':', passwd)

print('\n---计数---',
      f'统计count---{tuple1.count(1)}',
      f'排序sorted(tuple)---{sorted(users)}',
      sep='\n')

# 赋值
a, *b, c = tuple1
print(
    f'\n---元组多个值赋值给变量---\n第一个参数赋值给a---{a},\n最后一个参数赋值给c---{c},\n中间参数赋值给b--{b}')

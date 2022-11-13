# f-string
print(f'\n---f-string---\n{[i for i in range(1,5)]}')

# 类型转换
l1 = [1,2,3,4] 
l2 = ['a','b','c','d']
s = 'JQK'
t = ('j','Q','K')
print(f'\n---tuple 元组---\n{tuple(l1)}',tuple(s),sep='\n')
print(f'\n---set 集合---\n{set(l1)}',set(s),sep='\n')
print(f'\n---repr 字符串---\n{repr(l1)}')
print(f'\n---dict 字典---\n{dict(zip(l1,l2))}',dict([('1',1),('2',2),('3',123)]),sep='\n')
print(f'\n---list 列表---\n{list(s)}',list(t),sep='\n')

# 推导式
print('\n---dict推导式---',{i:i**2 for i in range(4,8)},sep='\n')
print('\n---list推导式---',f'偶数--{[i for i in range(10) if i % 2 == 0]}',sep='\n')
print('\n---set推导式---',{i for i in range(4,8)},sep='\n')
print('\n---tuple推导式---',tuple(i for i in range(4,8)),sep='\n') # 需要使用tulpe()
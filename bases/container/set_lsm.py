# 集合
'''
存储元素不重复,无序数据类型,只支持成员操作赋,for,枚举
无序的数据类型，添加顺序和在集合中的存储顺序不一样
不支持索引，重复，连接，切片
'''

# 推导式
print('\n---推导式---',{i for i in range(4,8)},sep='\n')


s = {1, 2, 4, 5}
s1 = set([])

print('\n---<class "set">---', type(s), sep='\n')
print('\n---空集合定义---', type(s1), sep='\n')
print('\n---判断---', 1 in s, sep='\n')
print('\n---枚举---')
for i, v in enumerate(s):
    print(i, v)
print('\n---迭代---', {i for i in s}, sep='\n')
s.add(10)  # 添加一个元素
s.update(['J', 'Q', 10])  # 添加多个元素
print('\n---增加---', s, sep='\n')
# s.pop()                           # 删除第一个元素
# s.remove(5)                      # 指定删除元素
print('\n---删除---', s, sep='\n')
# 关系
s2 = {'J', 'Q', 'k', 1}
print('\n---交集---', s.intersection(s2), s & s2, sep='\n')
print('\n---并集---', s.union(s2), s| s2, sep='\n')
print('\n---差集---',
      f's-s&s2---{s.difference(s2)}',
      f's2-s&s2---{s2.difference(s)}',
      sep='\n')
s3 = {1, 2}
s4 = {1, 2, 3}
print('\n---超集---',
      F's4是s3的超集---{s4.issuperset(s3)}',
      f's3是s4的子集---{s3.issubset(s4)}',
      sep='\n')

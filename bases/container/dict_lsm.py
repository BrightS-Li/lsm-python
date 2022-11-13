# 推导式
print('\n---推导式---',{i:i**2 for i in range(4,8)},sep='\n')

# 字典
dicts = {'a': {'name': 'li', 'age': 39, 'score': 59}, 'b': 'JQK'}
d = dict()

# 查看
print('\n---查看---',
      dicts['a']['age'],
      dicts.items(),
      dicts.get('d', 'key不存在'),
      sep='\n')

# fromkeys
print('\n---fromkeys所有值都一样---', {}.fromkeys({'1', '2'}, '000'), sep='\n')

# 判断
print('\n---判断---', 'age' in dicts, sep='\n')

# 迭代
print('\n---迭代key和value---')
for key in dicts:
    print(key, dicts[key])

for k, v in dicts.items():
    print(k, v)

print('\n---迭代value---')
for v in dicts.values():
    print(v)

# 增加
dicts['c'] = 'X'
print('\n---增加---', dicts, sep='\n')

# 删除
dicts.pop('c')
print('\n---删除---', dicts, sep='\n')

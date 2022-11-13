# 列表
import random

# 推导式
print('\n---推导式---',f'偶数--{[i for i in range(10) if i % 2 == 0]}',sep='\n')


list1 = [10, 'j', 'Q', 'K', 'A']

# 索引
print('\n---索引---',
      f'最后----{list1[-1]}\n最后之前所有----{list1[:-1]}\n倒叙输出----{list1[::-1]}',
      sep='\n')
# 判断包含元素
print('\n---判断---', 'j' in list1, 'B' in list1, sep='\n')  # 判断是否包含此元素
# 拼接
print('\n---拼接---', ['8', '9'] + list1, sep='\n')
# 嵌套
lists = [[1, 2, 3], [4, 5, 6], [list1]]
print('\n---嵌套---', lists[1][2], lists[2], lists[:][2], sep='\n')

# 增加
list1.append(9)
list1.extend(['1', '2'])
list1.insert(0, 8)
print('\n---添加---', f'添加一个9到最后,添加多个元素到最后,第一个位置添加8--{list1}', sep='\n')

# 删除
# list1.pop()
# list1.pop(0)
# list1.remove('1')
print('\n---删除---', f'弹出最后一个元素,弹出第一个元素,删除指定元素1--{list1}', sep='\n')

# 赋值
list1[0] = 3
list1[-2:] = [3, 4]
print('\n---赋值---', f'通过索引，重新赋值---{list1}', sep='\n')

# 查看
print('\n---查看---',
      f'list1--{list1}',
      f'查看count---{list1.count(3)}',
      f'查看位置---{list1.index("A")}',
      f'指定范围---{list1.index(3,0,-1)}',
      sep='\n')

# 排序
names = ['Bob', 'alice', 'coco', 'Harry']
names.sort()
print('\n---字母排序---', f'先大写排序---{names}', sep='\n')
names.sort(key=str.lower)  # 不区分大小写（先转换成小写，在排序）
print('\n---字母排序---', f'不区分大小写---{names}', sep='\n')

# 乱序
random.shuffle(list1)
print('\n---乱序---', f'random.shuffle---{list1}', sep='\n')

# 创建列表
list2 = [i for i in range(1, 5)]
list3 = list(range(1, 9))
print('\n---创建列表---', list2, list3, sep='\n')

# 去重
li = [1,2,3,1,4,5,2,4,7]
print('\n---转换成集合，去重---',list(set(li)),sep='\n')
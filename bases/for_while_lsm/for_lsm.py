# for

age = int(input('请输入你的年龄：'))

if age < 12:
    print('婴幼儿')
elif age >= 12:
    print('青少年')
elif age >=18 and age < 30:
    print('成年人')
elif age >= 10 and age < 50:
    pass # 跳过 不处理
else:
    print('老年人')
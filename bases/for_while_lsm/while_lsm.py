# whilie

# 不知道循环次数
prompt = '\n输入一些内容,系统将原样返回给你'
prompt += '\n键入quit,结束此程序运行\n---'
message = ''
# 使用判断while循环退出
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# 使用break退出循环
# while True:
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
#     else:
#         break

# continue 循环继续
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:  # 判断是否是偶数
        continue    # 如果是偶数，就放弃后面代码，继续循环
    print(a) # 打印基数 1，3，5，7，9
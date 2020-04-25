# 首先，创建一个待验证的列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ["Alice", "Cindy", "Marry"]
confirmed_users = []

# 验证每个用户，直到没有未验证的用户为止
# 将每个经过验证的用户都迁移到已验证的用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所有已经验证的用户
print("\nThe following users have been confirmed: ")
for confirmed_users in confirmed_users:
    print(confirmed_users, end="\t")

print()

# 列表中的remove函数删除所有列表中指定值的元素
pets = ['dog', 'cat', 'bird', 'fish', 'dog', 'cat', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 使用用户输入来填充字典
responses = {}
# 设置一个标志，指出调查是否应该继续
polling_active = True
while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat's is your name?")
    response = input("Which mountain would you like to climb someday?")

    # 将答案存储在responses中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person response(y/n)? ")
    if repeat == 'n':
        polling_active = False

print(responses)
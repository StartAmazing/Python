# message = input("tell me some message, and I'll repeat it to you: ")
# print(message)

prompt = "If you tell us who you are, we can personalize the message you see."
prompt = prompt + "\nWhat's your first name ?"

# name = input(prompt)
# print("hello, " + name)

# 使用int()来获取数值输入
# age = input("How old are you? ")
# age = int(age)
# print(age >= 17)

# 利用求模运算符来判断奇数还是偶数
number = input("please input a number: ")
number = int(number)
if number % 2 == 0:
    print("{} 是个偶数".format(number))
else:
    print("{} 是个奇数".format(number))
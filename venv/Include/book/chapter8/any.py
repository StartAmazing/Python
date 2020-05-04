print("--------------  传递任意数量的参数 --------------")
# 有时候不知道函数究竟会接受多少个参数, 使用*加上参数名就能将所接收到的参数封装到一个元组里面
def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

print("------------ 结合使用位置参数和任意数量实参 -------------")
# 如果要让函数接收不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后，Python
# 先匹配位置实参和关键字实参，再将剩余的实参都收集到最后一个实参中

def make_size_pizza(size, *toppings):
    print("\n make {} \n - inch pizza with the following toppings: ".format(str(size)))
    print("\t", end="")
    for topping in toppings:
        print(topping, end=",\t")

make_size_pizza(19)
make_size_pizza(18, 'A', 'B', 'C')

print()
print("-------------- 使用任意数量的关键字实参 -----------------")
#有的时候，需要编写任意数量的实参，但是预先不知道传递给函数的会是什么样的信息。在这种情况下
#可将函数编写成能够接受任意数量的唯一键值对---调用语句提供了多少就接受多少
def build_profile(**user_info):
    profile = {}
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile(firstName = 'albert', lastName = 'einstein',
                             location = 'new york', field = 'physics');

print(user_profile)



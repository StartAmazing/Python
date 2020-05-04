# 使用函数和while循环
def get_full_name(firstname: str, lastname: str):
    return firstname.title() + " " + lastname.title()

while True:
    print("\nPlease tell us your name: ")
    print("(enter 'q' at anytime to exit)")

    f_name = input("\n Input your first name: ")
    l_name = input("\n Input your last name: ")

    if f_name == 'q' or l_name == 'q':
        break

    fullname = get_full_name(f_name, l_name)
    print(fullname)

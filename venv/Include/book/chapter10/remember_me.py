import json
# 如果以前存储了用户名，就加载它
# 否则就提示用户输入并存储它
def greet_user():
    file_name = 'username.json'
    try:
        with open(file_name) as username_obj:
            username = json.load(username_obj)
    except FileNotFoundError:
        username = input("What's your name ? ")
        with open(file_name, 'w') as username_obj:
            json.dump(username, username_obj)
            print("We'll remember you when you come back, {}".format(username))
    else:
        print("welcome back, {}".format(username))

# greet_user()

print("-------------------------------")
def get_stored_username():
    '''如果存储了用户名那么句获取它'''
    file_name = "username.json"
    try:
        with open(file_name) as username_obj:
            username = json.load(username_obj)
    except:
        return None
    else:
        return username


def greet():
    '''问候用户，并指出其名字'''
    user_name = get_stored_username()
    if user_name == None:
        get_new_username()
    else:
        print("welcome back! {}".format(user_name))

def get_new_username():
    user_name = input("Please input your name: ")
    file_name = "username.json"
    with open(file_name, 'w') as file_obj:
        json.dump(user_name, file_obj)

greet()
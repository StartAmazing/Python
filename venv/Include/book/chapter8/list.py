def greet_users(names: list):
    for name in names:
        msg = "hello, {} !".format(name.title())
        print(msg)

usernames = ['alice', 'bob', 'cindy']
greet_users(usernames)

print("---------------------- 在函数中修改列表 -----------------")
print("---------------------- 不用函数的版本 -----------------")
unprinted_designs=['iphone case', 'robot pendent', 'dodecahedron']
completed_models=[]

print(unprinted_designs)
print(completed_models)

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("current design is: {}".format(current_design.title()))
    completed_models.append(current_design)

print(unprinted_designs)
print(completed_models)
print("---------------------- 使用函数的版本 -----------------")
def print_models(unprinted_designs, completed_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("current design is: {}".format(current_design))
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been designed: ")
    for model in completed_models:
        print(model, end="\t")
    print()

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print("-------------------------------- 禁止函数修改列表 ---------------------------")
unprinted_designs = ['A', 'B', 'C']
print_models(unprinted_designs[-1::-1], completed_models)
print(unprinted_designs)
print(completed_models)
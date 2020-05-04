# 姓名
def get_formatted_name(first_name: str, last_name: str):
    full_name = first_name.title() + " "+ last_name.title()
    return full_name

musician = get_formatted_name("jimi", "hendrix")
print(musician)

# 函数返回字典
def build_person(firstname: str, lastname: str, age: int = 0) -> dict:
    # 返回一个字典，其中包含有关一个人的信息
    person = {'first': firstname, 'last': lastname}
    if age != 0:
        person['age'] = age
    return person

print(build_person('Lisa', 'Smith'))
print(build_person('Lisa', 'Smith', 18))
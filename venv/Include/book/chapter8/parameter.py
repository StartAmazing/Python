# 让实参变成可选的
def get_formatted_name(firstname: str, lastname: str, middlename=''):
    fullname = firstname.title() + " " + middlename.title() + " " + lastname.title()
    if middlename == '':
        fullname = firstname.title() + " " + lastname.title()

    return fullname.title()

musician = get_formatted_name(firstname="john", middlename='lee', lastname='hooker')
print(musician)

musician = get_formatted_name("Alice", "Smith")
print(musician)

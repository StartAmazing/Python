# 姓名
def get_formatted_name(first_name: str, last_name: str):
    full_name = first_name.title() + " "+ last_name.title()
    return full_name

musician = get_formatted_name("jimi", "hendrix")
print(musician)
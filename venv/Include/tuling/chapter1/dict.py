# 字典
print("--------------------------- basic use -----------------------")
alien_0 = {'color': 'green', 'points': '5'}
print(alien_0['color'])
print(alien_0['points'])

new_gard = alien_0['points']
print("your just earned {} points!".format(str(new_gard)))

print("------------------------- operations -------------------------")
print(alien_0)
alien_0['name'] = 'Alice'
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 创建新的字典
alien_0 = {}
print(type(alien_0))

alien_0 = dict()
print(type(alien_0))
alien_0['color'] = 'yellow'
alien_0['points'] = 10
print(alien_0)

alien_0['color'] = 'red'
print('current alien\'s color is {}'.format(alien_0['color']))
alien_0['color'] = 'black'
print('current alien\'s color is {}'.format(alien_0['color']))

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('Origin x-position: ' + str(alien_0['x_position']))

# 向右移动外星人
# 根据外星人当前的速度决定将其移动多远
x_increment = 0
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x-position: ' + str(alien_0['x_position']))

print(alien_0)
del alien_0['speed']
print(alien_0)

print("---------------------- anthor method of use ----------------")
# 使用一个字典存储众多对象的同一种信息
favorite_languages = {
    'Alice': 'c',
    'Bob' : 'c ++',
    'Cindy' : 'ruby',
    'Divid' : 'python',
    'Eric' : 'python',
    'Frank' : 'java'
}

print(favorite_languages)
print("Alice's favorite language is {}.".format(favorite_languages['Alice'].title()))

print("------------------------ simple test1 --------------------")
# 1.
aWei = {}
aWei['first_name']='wei'
aWei['last_name']='huang'
aWei['age']=23
aWei['live_city']='beijing'
print(aWei)

# 2.
favorite_number = {}
favorite_number['liuliang'] = 7
favorite_number['dulinfeng'] = 3
favorite_number['chenzhi'] = 9
favorite_number['chenlang'] = 6
favorite_number['huangwei'] = 1
print(favorite_number)

print("---------------------- traverse the dict --------------------")
user_0 = {
    'username': 'efermi',
    'first' : 'enrico',
    'last' : 'fermi'
}

for key,value in user_0.items():
    print("key is {} and value is {}.".format(key, value))

for name,language in favorite_languages.items():
    print("\n name is {} and she(he) likes {} best!".format(name,language))

friends = ['Alice','Eric']
for name in favorite_languages.keys():
    print("name: {}".format(name))
    if name in friends:
        print("Hi, {}, I see your favorite is {}!".format(name, favorite_languages[name].title()))

for language in favorite_languages.values():
    print("languages: {}".format(language.title()))

if 'Erin' not in favorite_languages.keys():
    print("Hi, Erin, please tell us your favorite language.")

print()

for name in sorted(favorite_languages.keys()):
    print("Hi, {}, please tell us your second favorite language!".format(name))

print()
print("The following language had been mentioned: ")
for language in favorite_languages.values():
    print(language.title())

print("The following language had been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())

print("------------------------ simple test2 --------------------")

print("------------------------ list contains dict --------------------")
alien_0 = {'color':'green', 'points': 5}
alien_1 = {'color': 'yellow','points': 7}
alien_2 = {'color': 'red', 'points': 10}

aliens = [alien_0, alien_1, alien_2]
print(aliens)

aliens = []
for alien_num in range(30):
    new_alien = {'color': 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print(" ... ")
print("total aliens is: {}".format(str(len(aliens))))

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['y_point'] = 10
        alien['point'] = 10

for alien in aliens[0:5]:
    print(alien)
print("...")
print("total aliens is: {}".format(str(len(aliens))))


for alien in aliens[0:4]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['y_point'] = 5
        alien['points']  = 20
    elif alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['y_point'] = 10
        alien['point'] = 10

for alien in aliens[0:5]:
    print(alien)
print("...")

print("------------------------ dict contains list --------------------")
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print("you ordered a {}-crust pizza with the following toppings: ".format(pizza['crust']))
for topping in pizza['toppings']:
    print(topping, end='\t')
print()
print()

favorite_languages = {
    "Alice": ["c", "java"],
    "Bob": ["c++", "scala"],
    "Cindy": ["ruby"],
    "David":["python", "golang", "java"],
    "Eric": ["java","golang"]
}
for name,all_language in favorite_languages.items():
    if len(all_language) == 1:
        print("\n {}'s favorite language is: ".format(name.title()))
    else:
        print("\n {}'s favorite languages are: ".format(name.title()))

    for language in all_language:
        print("\t{}".format(language.title()))

print("------------------------ dict contains dict --------------------")
users = {
    'aeinstrin': {
        'first': 'albert',
        'last': 'einstrin',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print("\nUsername: {}".format(username))
    full_name = user_info['first'].title() + " " + user_info['last'].title()
    location = user_info['location']

    print("\tFull name: {}".format(full_name))
    print("\tLocation: {}".format(location.title()))



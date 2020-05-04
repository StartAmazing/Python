from collections import OrderedDict

favorite_langurage = OrderedDict()

favorite_langurage['jen'] = 'python'
favorite_langurage['sarah'] = 'c'
favorite_langurage['edward'] = 'ruby'
favorite_langurage['phil'] = 'python'

for name,value in favorite_langurage.items():
    print(name.title() + "'s favorite language is " + value.title())

print("==========================================")
favorite_langurage_notordered = {}

favorite_langurage_notordered['jen'] = 'python'
favorite_langurage_notordered['sarah'] = 'c'
favorite_langurage_notordered['edward'] = 'ruby'
favorite_langurage_notordered['phil'] = 'python'

for name,value in favorite_langurage_notordered.items():
    print(name.title() + "'s favorite language is " + value.title())
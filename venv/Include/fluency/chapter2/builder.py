print("------------------------- builder ---------------")
print("生成器表达式： ")

symbols = '$¢£¥€¤'

tuple = tuple(ord(symbol) for symbol in symbols)
print(tuple)

import array
array = array.array('I', (ord(symbol) for symbol in symbols))
print(array)

print("------------------------------------------")
colors = ["White", "Black"]
sizes = ["S", "M", "L"]
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

tshirts = ('%s %s' % (c, s) for c in colors for s in sizes)
print(tshirts)
print(type(tshirts))
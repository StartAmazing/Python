print("----------------------- with listcomps ---------------")
symbols = '$¢£¥€¤'

codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
print(beyond_ascii)

print("----------------------- with lambda ---------------")
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

print("----------------------- with dicar ---------------")
print("使用列表推导计算笛卡尔积： ")
colors = ["White","Black"]
sizes = ["S", "M", "L"]
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)
tshirts = [(size, color) for color in colors for size in sizes]
print(tshirts)
tshirts = [(size, color) for size in sizes for color in colors]
print(tshirts)
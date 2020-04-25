# 元组
#  可以理解成一个不允许更改的列表

print("------------------ tuple --------------------")
ta = ()
print(type(ta))
tb = (100)
print(type(tb))
tc = (100,)
print(type(tc))
td = (100, 200, 300, 400)
print(type(td))

# 直接用逗号
te = 100,
print(type(te))
tf = 100, 200, 300
print(type(tf))

# 3. 使用tuple定义
th = tuple()
print(type(th))
li = [1, 2, 3, "HELLO"]
ti = tuple(li)  # 要求tuple必须可迭代
print(li)
print(ti)

print("--------------- operations --------------------")
la = ["i", "love", "Alice"]
print(la)
ta = tuple(la)
print(ta)

# tuple 分片操作
print(ta[:])
print(ta[:2])
print(ta[-1::-1])

# 元组的相加
ta = 100, 200, 300
tb = ("hello", "world")
tc = ta + tb
print(tc)

td = tb * 2
print(td)

# tuple成员检测，判断是否在元组中
print(tb)
print("hello" in tb)

# 元组的遍历
for ele in tb:
    print(ele)

# 元组可以嵌套
print("-------------------- tuple in tuple -------------------")
ta = ((10, 20, 30), ("hello", "Alice", "Bob"), (100, 200, 300))
for i in ta:
    for j in i:
        print(j, end=", ")
    print()

for i in ta:
    print(i)

# 这种访问有一个规定，即i, j, k要跟元组的元素个数对应
for i, j, k in ta:
    print(i, j, k)

print("------------------------- func -------------------------")
print(len(ta))
print(max(ta[0]))
print(min(ta[0]))

tb = (1, 2, 3, "love", 11, 23, 1, 2, 1)
print(tb[3])

# count: 对某一元素计数
print(tb.count(1))
# index: 某一元素的位置
print(tb.index(3))

# tuple的特殊用法
a = 100
b = "alice bob"
# 要求交换a, b 的值
# c此用法是python的特性
a, b = b, a
print(a)
print(b)

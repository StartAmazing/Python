'''
    str
    list
    tuple
    set
    dict
'''

print("--------------  list列表  -------------------")
# 一组有序数据组成的序列,用中括号直接创建，内容用英文逗号隔开
l1 = [1, 2, 3, 4, 5]
l2 = ["Alice", "Bob", 2, "Cindy", True, None]
print(l1)
print(l2)
# 创建列表的第二种方式，使用list创建
l3 = []
l4 = list()
print(l3)
print(l4)
print(type(l3))
print(type(l4))
# 特例，如果列表中包含单个字符串的话...
s = "Alcie Smith"
# 想创建一个只包含s一个字符串的列表
l5 = [s]
l6 = list(s)
print(type(l5))
print(l5)
print(type(l6))
print(l6)

print("--------------  list列表常用操作  -------------")
# 列表的常见操作
# 使用下标操作，也叫索引
# 列表的元素索引是从0开始
l1 = [32, 33, 45, 112, 34]
# 使用下标访问，注意下标越界
# 注意IndexError引发的原因
print(l1[4])

# 切片操作
l2 = l1[2:]
print(l2)
l3 = l1[-3:-1]
print(l3)
print(l1[-1:-3:-1])

print(id(l2))
print(id(l1))

l4 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l5 = l4[1:8:2]
print(l5)
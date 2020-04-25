print("------------------- set ----------------")
# 跟数学中集合的概念一直，内容无序 + 无重复
# 集合的定义
# 通过set关键字
sa = set()
print(type(sa))

list = [1, 2, 3, 4, 5, 6, 6, 6, 7, 7]
sb = set(list)
print(sb)

# 使用大括号
sc = {1, 2, 3, 4, 5, 6, 6, 7}
print(sc)

print("--------------------- operations ---------------------")
print(1 in sc)

for i in sc:
    print(i, end=" ")
print()

sd = {1, 45, 2, 334, 24, 112, 45, "Alice"}
print(sd)

# 集合的另一种遍历
se = {(1, 2, 3), (23, 11, 24), ("Alice", "Bob", "Cindy")}
for i,j,k in se:
    print(i,j,k, end=" ")
print()

# 集合的生成式
sa = {1,2,4,233,123,45,12}
sb = {i for i in sa}
print(sb)

sc = {i for i in sa if i % 2 == 0}
print(sc)

# 双重for 循环
sd = {i**2 for i in sa}
print(sd)

se = {i * j for i in sa for j in sa}
print(len(se))
print(se)

sf = set()
for i in sa:
    sf.add(i ** 2)
print(sf)

# clear 清空
# 删除操作
# remove 和discard的区别
print(sa)
sa.remove(1)
print(sa)
print(sa.remove(2))

# remove删除的值如果不在集合中，那么直接报错
sa.discard(5)
print(sa.discard(5))

# pop
print(sa)
sa.pop()
print(sa)

# 集合的运算操作
print("--------------------------- calculation set --------------------------")
sa = {1,2,3,4}
sb = {"Alice", "Bob", "Cindy"}
print(sa.intersection(sb))
print(sa.difference(sb))
print(sa.union(sb))

# 冰冻集合
# 不允许修改此集合
print(sa)
sb = frozenset(sa)
print(sb)

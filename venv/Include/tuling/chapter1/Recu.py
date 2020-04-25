def func_a(n):
    if n == 1:
        return 1
    return n * func_a(n - 1)


print(func_a(5))

# 斐波那契数列
def feboo(n):
    if n == 1 or n == 2:
        return 1
    return feboo(n - 1) + feboo(n - 2)


print(feboo(6))

# 汉诺塔
a = 'A'
b = 'B'
c = 'C'
def hanoo(a, b, c, n):
    if n == 1:
        print("{} -> {}".format(a, c))
        return None
    if n == 2:
        print("{} -> {}".format(a, b))
        print("{} -> {}".format(a, c))
        print("{} -> {}".format(b, c))
        return None
    hanoo(a, c, b, n - 1)
    print("{} -> {}".format(a, c))
    hanoo(b, a, c, n - 1)

hanoo(a, b, c, 3)
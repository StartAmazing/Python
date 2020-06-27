a, *b = 'spam'
print(a)
print(b)
c, d = 'spam', 'spam'
print(c)
print(d)
a, b, c, d = 'spam'
print(a)
print(b)
print(c)
print(d)

print("---------------")
[a, b, c] = (1, 2, 3)
print(a)
print(b)
print(c)

print("---------------")
string = "SPAM"
a, b, c, d = string
print(a)
print(b)
print(c)
print(d)

print("---------------")
a, b, c = string[0], string[1], string[2:]
print(a)
print(b)
print(c)

print("---------------")
a, b, c = list(string[:2]) + [string[2:]]
print(list(string[:2] + string[2:]))
print(list(string[:2]) + [string[2:]])
print(a)
print(b)
print(c)

print("---------------")
a, b = string[:2]
c = string[2:]
print(a)
print(b)
print(c)

print("---------------")
(a, b), c = string[:2], string[1:]
print(a)
print(b)
print(c)

print("---------------")
red, blue, yellow = range(3)
print(red)
print(blue)
print(yellow)
print(list(range(3)))

print("---------------")
L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)

print("---------------")
seq = [1, 2, 3, 4]
a, b, c, d = seq
print(a, b, c, d)

print("---------------")
a, *b = seq
print(a, b)
*a, b = seq
print(a, b)
a, *b ,c = seq
print(a, b, c)
a, b, c, *d = seq
print(a, b, c, d)

print("---------------")
a, *b = 'spam'
print(a, b)
a, *b, c = 'spam'
print(a, b, c)
a, *b, c = range(7)
print(a, b, c)

print("---------------")
L = [1, 2, 3, 4]
while L:
    front, *L = L
    print(front, L)

print("---------------")
for (a, *b, c) in ([1, 2, 3, 4], [5, 6, 7, 8]):
    print(a, b, c)

print("---------------")
a = b = c = 'spam'
print(a, b, c)

print("---------------")
a = b = 0
b += 1
print(a, b)

a = b = []
a.append(42)
print(a, b)

a = []
b = []
# a, b = [], []
a.append(42)
print(a, b)

print("---------------")
L = [1, 2]
L = L + [3]
print(L)
L.append(4)
print(L)
L += [5, 6]
print(L)
L = L + [7, 8]
print(L)
L.extend([9, 10])
print(L)

print("---------------")
L = []
# '+='(extend)接受任意的序列，而拼接一般情况下不接受不同的的序列
L += 'spam'
L += ('a', 'c')
print(L)
# L = L + ('e', 'g') # Error
# L = L + 'spam' # Error
L = L + list('spam')
print(L)
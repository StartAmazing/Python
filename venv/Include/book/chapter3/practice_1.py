friends = ["Alice", "Bob", "Cindy"]
print(friends)

print("hello " + friends[0])
print("hello " + friends[1])
print("hello " + friends[2])

friends[0] = "Huang Wei"
friends.append("Ai Xingba")
print(friends)

friends.insert(0, "Chen Lang")
print(friends)

del friends[2]
print(friends)

friends.append("Eric")
print(friends)

person = friends.pop()
print("the last del friend is " + person)
print(friends)

girl = friends.pop(2)
print("the last del girl is " + girl)
print(friends)

friends.insert(3,"Jerry")
print(friends)

friends.remove("jerry".title())
print(friends)

friends.append("lullaby".title())
print(friends)

friends.sort()
print(friends)

friends.sort(reverse = True)
print(friends)

print("here is all my friends: ")
print(sorted(friends, reverse=True))

print(friends)

friends = ['Chen Lang', 'Huang Wei', 'Cindy', 'Ai Xingba', 'Eric']
print(friends)
friends.reverse()
print(friends)

print(len(friends))

for name in friends:
    print(name + ", this is my best friend!")
    print(name + ", this is a cool friend!")

print("thanks all my friend")

for val in range(1,4):
    print(val)

numbers = list(range(1,4))
print(numbers)

numbers = list(range(2,11,2))
print(numbers)

spares=[]
for i in range(1, 11):
    spares.append(i ** 2)

print(spares)

print(min(spares))
print(max(spares))
print(sum(spares))

spares = [values ** 2 for values in numbers]
print(spares)

numbers = list(range(1,21))
print(numbers)

#始终包含左边的元素而不会包含右边的元素
print(friends)
print(friends[0:3])
print(friends[-3:-1])
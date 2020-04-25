# 继承
class Person1():
    pass

class Person2(object):
    pass

class Creature(object):
    pass

class Person(Creature):
    name = "NoName"
    age = 0

class Teacher(Person):
    pass

t = Teacher()
print(t.name)

class Bird(Creature):
    fly = "yes, all we can"
    def flying(self):
        print("you ought to fly fly step into the night!")

class BirdMan(Person, Bird):
    pass

bm = BirdMan()
bm.flying()
print(bm.name)

# issubclass检测是否是子类
# 可以用来检测两个类的父子关系
print(issubclass(BirdMan, Bird))
print(issubclass(BirdMan, Person))
print(issubclass(Bird, Person))
print(issubclass(BirdMan, Creature))

# 构造函数默认继承
class Dog():
    name = "None"
    age = -1
    def __init__(self,name,age):
        self.name = name
        self.age = age

class SpottyDog(Dog):
    pass

shilubi = SpottyDog("Shilubi", 3)
print(shilubi.name)
print(shilubi.age)
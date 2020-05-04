class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting!")

    def roll_over(self):
        print(self.name.title() + " is rolling over!")

my_dog=Dog('xiaohua', 7)
print("my dog's name is {}, and she's age is {}".format(my_dog.name.title(), str(my_dog.age).title()))
my_dog.sit()
my_dog.roll_over()
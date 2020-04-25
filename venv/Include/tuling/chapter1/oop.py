# 定义类
class Student():
    pass

# 定义一个对象
alice = Student()

#
class PythonStudent():
    name = "NoOne"
    age = 18
    course = "Python"

    def giveMeMoney(self):
        print("Show me the money")
        return None

bob = PythonStudent()
print(bob.name)
print(bob.age)
print(bob.course)
bob.giveMeMoney()
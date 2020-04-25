# 类的例子
# 注意类的定义
class Student():
    name = "Peking University"
    age = 19

    def sayHi(self):
        self.name = 'Beijing University'
        print("I love {}".format(self.name))
        return None

    def sayHello():
        print("My school is {}".format(__class__.name))
        return None

# 实例化
Alice = Student()
print(Alice.name)
Alice.sayHi()

# 类的变量作用于的问题
# 类变量： 属于类自己的变量
# 实例变量： 属于实例的变量
print(Student.name)
Alice.name = "Oxford University"
print(Alice.name)
Student.sayHi(Alice)
print(Student.name)

Student.sayHello()

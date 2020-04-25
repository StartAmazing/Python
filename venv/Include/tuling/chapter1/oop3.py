# 构造函数
# 类在实例化的时候，执行一些基础性的初始化工作
# 使用特殊的名称和写法
class Student():
    name = "NoName"
    age = 0

    #构造函数名称固定，写法相对固定
    def __init__(self,name):
        self.name = name
        print("我是构造函数")
        return None

Alice = Student("Alice")
print("--------------------")
print(Alice.name)
print(Alice.age)
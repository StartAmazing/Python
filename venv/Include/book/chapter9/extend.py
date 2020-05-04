'''
    编写类的时候，并非总是要从空白开始。如果你想要编写的类是另一个现成类的特殊版本
    ，可以使用继承。一个类继承另一个类的时候，他将自动获得另一个类的所有属性和方法
    ；原有的类被称父类，现在的类被称为父类，同时还可以定义自己的属性和方法
'''

# 创建子类的时候，Python首先要完成的任务是给父类的所有属性赋值。为此，子类的方法
# __init__需要父类施以援手
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptiv_name(self):
        long_name = str(self.year) + ' ' + self.model + ' ' + self.make
        return long_name.title()

    def get_odometer(self):
        print('this car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, miles):
       if self.odometer_reading < miles:
           self.odometer_reading = miles
       else:
           print("you can't roll your metter back !!!")

    def increament_odometer(self, mile):
        self.odometer_reading += mile

    def fill_gas_tank(self):
        print("this is a car which need fill_gas_tank. ")

class Battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This is a car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += "miles on a full charge. "
        print(message)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # 给子类定义独有的属性
        self.battery_size = 70

        # 使用实例作为类的一个属性
        self.battery = Battery()

    def describ_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        print("this car which don't need fill_gas_tank. ")




my_tasla = ElectricCar('tesla', 'model s', 2016)
print(my_tasla.get_descriptiv_name())
my_tasla.describ_battery()
my_tasla.fill_gas_tank()
my_tasla.battery.describe_battery()
my_tasla.battery.get_range()



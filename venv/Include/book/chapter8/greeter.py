def greeter():
    print("hello, method!")

greeter()

def greeter(username: str):
    print("hello, {}".format(username.title()))

greeter('cindy')

# 位置传参
def describ_pet(pet_name:str, animal_type:str='dog'):
    print("\nI have a {}.".format(animal_type))
    print("My {}'s name is {}".format(animal_type, pet_name.title()))

type = 'dog'
name = 'huahua'
describ_pet(animal_type=type, pet_name=name)
describ_pet(pet_name=type, animal_type=name)

# 形参的默认值
describ_pet(pet_name='xiaohua')
describ_pet('xiaomahua')
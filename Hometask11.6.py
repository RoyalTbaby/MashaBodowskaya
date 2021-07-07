"""
Добавить в метод инициализации новый приватный атрибут - master. Создать метод get_master() который
возвращает значение атрибута master.
"""


class Dog:
    def __init__(self, height, weight, name, age, master):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.__master = master

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def bark(self):
        print('Woof Woof!')

    def get_master(self):
        return self.__master

    def set_master(self, master):
        self.__master = master


dog1 = Dog(120, 43, 'Bubblegum', 3, 'Jimmy')
print(f"The dog's name is {dog1.name}")
print(f"The dog's height is {dog1.height}")
print(f"The dog's weight is {dog1.weight}")
print(f"The dog's age is {dog1.age}")
print(dog1.get_master())
dog1.set_master('Timmy')
print(dog1.get_master())
dog1.run()
dog1.jump()
dog1.bark()

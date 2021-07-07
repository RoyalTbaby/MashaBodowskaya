"""
Сделать все атрибуты класса Dog приватными. Сделать для каждого атрибута getter и setter используя
декораторы. Все change методы удалить
"""


class Dog:
    def __init__(self, height, weight, name, age, master):
        self.__address = "Minsk"
        self.__height = height
        self.__weight = weight
        self.__name = name
        self.__age = age
        self.__master = master

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def bark(self):
        print('Woof Woof!')


dog1 = Dog(120, 43, 'Bubblegum', 3, 'Jimmy')
print(dog1.name)
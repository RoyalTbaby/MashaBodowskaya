"""
Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет атрибут имени у
объекта. Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.
"""


class Dog:
    def __init__(self, name):
        self.name = name

    def change_name(self, name):
        self.name = name


dog_1 = Dog('Fatima')
print(dog_1.name)
dog_1.change_name('Izzie')
print(dog_1.name)
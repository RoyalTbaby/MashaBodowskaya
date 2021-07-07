"""
Создать три класса: Dog, Cat, Parrot. Атрибуты каждого класса: name, age, master. Каждый класс содержит
конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep.
Класс Parrot имеет дополнительный метод fly. Cat - meow, Dog - bark.
"""


class Dog:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def birthday(self, age):
        self.age = self.age + 1
        return self.age

    def bark(self):
        print('Woof Woof!')

    def sleep(self):
        print('Sleep!')


doggie = Dog('Willy', 12, 'Sarah')
print(doggie.birthday(0))


class Cat:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def birthday(self, age):
        self.age = self.age + 1
        return self.age

    def meow(self):
        print('Meow Meow!')

    def sleep(self):
        print('Sleep!')


cat1 = Cat('Tara', 2, 'Masha')
print(cat1.birthday(0))


class Parrot:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def birthday(self, age):
        self.age = self.age + 1
        return self.age

    def fly(self):
        print('Fly!')

    def sleep(self):
        print('Sleep!')


coco = Parrot('Siena', 7, 'Rory')
print(coco.birthday(0))
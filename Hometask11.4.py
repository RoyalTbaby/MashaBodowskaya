"""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age. Класс
имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран. Создать
объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.
"""


class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def bark(self):
        print('Woof Woof!')


dog1 = Dog(120, 43, 'Bubblegum', 3)
print(f"The dog's name is {dog1.name}")
print(f"The dog's height is {dog1.height}")
print(f"The dog's weight is {dog1.weight}")
print(f"The dog's age is {dog1.age}")
dog1.run()
dog1.jump()
dog1.bark()
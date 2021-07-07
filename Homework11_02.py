"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные.
"""


class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = 0

    def speed_up(self):
        self.__speed = self.__speed + 5

    def speed_down(self):
        self.__speed = self.__speed - 5

    def stop(self):
        self.__speed = 0

    def get_speed(self):
        return self.__speed

    def turn(self):
        pass


car1 = Car('Chevy', 'Corvette', 2021)
print(car1.get_speed())
car1.speed_up()
print(car1.get_speed())
car1.speed_up()
print(car1.get_speed())
car1.speed_down()
print(car1.get_speed())
car1.get_speed()
print(car1.stop())
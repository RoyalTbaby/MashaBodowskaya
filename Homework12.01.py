"""
1. Создать класс MyTime. Атрибуты: hours, minutes, seconds. Методы:
переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три
числа, другой объект класса MyTime, и отсутствие входных параметров.
Реализовать нормальное отображение времени(12:65:83 - 13:06:23)
[my-oop-02]
"""

import datetime
from datetime import timedelta
from datetime import datetime, time

class Mytime:
    def __init__(self, hours, minutes, seconds):
        self.__time = datetime(1, 2, 1, hour=hours, minute=minutes, second=seconds)
        self.hours = self.__time.hour
        self.minutes = self.__time.minute
        self.seconds = self.__time.second

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    def __eq__(self, other):  # Определяет поведение оператора равенства, ==
        if isinstance(other, Mytime):
            return self.hours == other.hours

        if isinstance(other, Mytime):
            return self.minutes == other.minutes

        if isinstance(other, Mytime):
            return self.seconds == other.seconds

        return False

    def __ne__(self, other):  # Определяет поведение оператора неравенства, !=
        if isinstance(other, Mytime):
            return self.hours != other.hours

        if isinstance(other, Mytime):
            return self.minutes != other.minutes

        if isinstance(other, Mytime):
            return self.seconds != other.seconds

        return False

    def __ge__(self, other):  # Определяет поведение оператора больше или равно, >=
        if isinstance(other, Mytime):
            return self.hours >= other.hours

        if isinstance(other, Mytime):
            return self.minutes >= other.minutes

        if isinstance(other, Mytime):
            return self.seconds >= other.seconds

        return False

    def __le__(self, other):  # Определяет поведение оператора меньше или равно, <=
        if isinstance(other, Mytime):
            return self.hours <= other.hours

        if isinstance(other, Mytime):
            return self.minutes <= other.minutes

        if isinstance(other, Mytime):
            return self.seconds <= other.seconds

        return False

    def __lt__(self, other):  # Определяет поведение оператора меньше, <
        if isinstance(other, Mytime):
            return self.hours < other.hours

        if isinstance(other, Mytime):
            return self.minutes < other.minutes

        if isinstance(other, Mytime):
            return self.seconds < other.seconds

        return False

    def __gt__(self, other):  # Определяет поведение оператора больше, >
        if isinstance(other, Mytime):
            return self.hours > other.hours

        if isinstance(other, Mytime):
            return self.minutes > other.minutes

        if isinstance(other, Mytime):
            return self.seconds > other.seconds

        return False

    def __add__(self, other):
        date1 = self.__time\
                + timedelta(hours=other.hours, minutes=other.minutes, seconds=other.seconds)
        return Mytime(date1.hour, date1.minute, date1.second)

    def __sub__(self, other):
        total_hours = self.hours - other.hours
        total_minutes = self.minutes - other.minutes
        total_seconds = self.seconds - other.seconds
        return Mytime(total_hours, total_minutes, total_seconds)

    def __mul__(self, other):
        total_hours = self.hours * other.hours
        total_minutes = self.minutes * other.minutes
        total_seconds = self.seconds * other.seconds
        return Mytime(total_hours, total_minutes, total_seconds)


test1 = Mytime(2, 0, 22)
test2 = Mytime(3, 44, 2)
test3 = test1 * test2
test4 = test1 > test2
print(test3)
print(test4)













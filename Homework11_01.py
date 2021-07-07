"""
Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода.
"""


class BankAccount:
    def __init__(self, name, amount, passport):
        self.__name = name
        self.__amount = amount
        self.__passport = passport

    def public_data(self):
        self.__protected_data()

    def __protected_data(self):
        print(self.__name, self.__amount, self.__passport)


account1 = BankAccount('Mary Rosenford', 3456, 'MC65432334')
account1.public_data()


def set_name(name):
    print(name)


def set_school(school):
    print(school)


class SchoolGrades:

    def __init__(self, grade, name, school):
        self.__grade = grade
        self.__name = name
        self.__school = school

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):

        if grade > 5:
            self.__grade = grade
            print(grade)
        else:
            print('Not Qualified')

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return name

    def get_school(self):
        return self.__school

    def set_school(self, school):
        self.__school = school
        return school

    def __str__(self):
        return self.__name + ' ' + self.__school


student_grade1 = SchoolGrades(0, 'Ron Wisley', 'Hogwarts')
print(student_grade1)


class EmployeesBirthday:
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.congrats = 'Happy {}s birthdays, dear {}'.format(self.__age, first_name)

    def get_congrans(self):
        return 'Happy {}s birthdays, dear {}'.format(self.__age, self.__first_name)

    def __str__(self):
        return "age {}, first_name {}, congrats '{}'".format(self.__age, self.__first_name, self.get_congrans())

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, newvalue):
        self.__age = newvalue


employee1 = EmployeesBirthday('Jeffrey', 'Paul', 33)
employee1.age = employee1.age + 1
print(employee1)
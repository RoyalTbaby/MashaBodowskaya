"""
Создать родительский класс Pet, содержащий все общие методы классов
Dog, Cat, Parrot. Унаследовать Dog, Cat, Parrot от класса Pet. Удалить в
дочерних классах те методы, которые имеются у родительского класса.
Создать объект каждого класса и вызвать все его методы.
"""


class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def sleep(self):
        print('Sleep!')


class Cat(Pet):
    pass


cat1 = Cat("De", 56, 'YTt')
print(cat1.name)
cat1.sleep()
cat1.run()
cat1.jump()


class Dog(Pet):
    pass


dog1 = Dog('Goro', 4, 'Tyoy')
print(dog1.age)
dog1.sleep()
dog1.jump()
dog1.run()


class Parrot(Pet):
    pass


birdy = Parrot('Roro', 47, 'Eva')
print(birdy.master)
birdy.sleep()
birdy.run()
birdy.jump()
"""
Создать lambda функцию, которая
принимает на вход имя и выводит его
в формате “Hello, {name}”
"""

name = lambda myname: f'Hello, {myname}'
your_name = name(input("Enter your name: "))
print(your_name)


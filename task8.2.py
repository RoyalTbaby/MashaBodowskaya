"""
Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую распознавать слова
палиндромы.)
"""


def check(string):
    if string == string[::-1]:
        return "There you go!"
    else:
        return "Sorry boo :("


words = ["Mamam", "betеy", "шаЛаШ"]
for word in words:
    print(check(word.lower()))
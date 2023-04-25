"""
DRY - don't repeat yourself - не повторяйся
YAGNI - You aren't gonna need it - это не понадобится (Вам это не понадобится)
KISS - Keep it simple, stupid - будь проще
POLA - Principle of Least Astonishment - не удивляй пользователя
EAFP - Easier to Ask for Forgiveness than Permission - проще извинится, чем просить разрешения (сначала действуй)
LBYL - Look Before You Leap - смотри, прежде чем прыгнуть (сначала спроси)
"""


def func():
    # some code
    return read_from_file('test.txt')


def two():
    # some code
    return read_from_file('test2.txt')


def read_from_file(name):
    with open(f'folder/{name}') as file:
        return file.readlines()


class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f"{self.name} says: Meow!")

    def scratch(self):
        # code
        pass


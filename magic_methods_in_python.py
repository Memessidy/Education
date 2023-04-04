# Магичесие методы = dunder методы, методы которые начинаются и заканчиваются ...
# init по умолчанию не ждёт аргументов
# repr - для программистов, возвращает строку, по которой видно (и можно воссоздать) состояние
# объекта
# str - для людей, возвращает строку
# если не реализованы repr и str, то будет возвращён адрес в памяти
# eq по умолчанию сравнивает адрес в памяти, в реализации лучше сразу проверить тип
# Если методы не реализованы, то падает ошибка
# contains для реализации проверки IN (перегрузка оператора in)
# bool для самодельных объектов всегда вернёт True, для изменения поведения нужно написать  __bool__
# len вернёт ошибку, если не переопределить метод __len__
# Чтобы объект стал вызываемым (callable) нужно реализовать __call__, иначе ошибка
# __iter__ возвращает объект- итератор, тот кто реализует iter = iterable
# __iter__ ВОЗВРАЩАЕТ ИТЕРАТОР
# __next__ должен вернуть слудющий объект из контейнера, кто реализует next = Iterator, for работает до StopIteration
# iter возвращает iterator, iterator должен иметь метод next
# __getitem__ нужен для функционала [] (аналог списка и словаря) - индексация
# __setitem__ нужен для причвоение через [] (присвоение по индексу), если не реализовать - ошибка
# если в объекте не реализован __iter__ то для цикла for будет использован __getitem__,
# там ожидается падение IndexError


class Banknote:

    def __init__(self, value: int):
        self.value = value

    # Для программистов
    def __repr__(self):
        return f'Banknote({self.value})'

    # Для людей
    def __str__(self):
        return f'Банкнота номиналом в {self.value} рублей'

    def __eq__(self, other=None):
        if other is None or not isinstance(other, Banknote):
            return False
        else:
            return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value


class Iterator:

    def __init__(self, container):
        self.container = container
        self.index = 0

    def __next__(self):
        if 0 <= self.index < len(self.container):
            value = self.container[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


class Wallet:

    def __init__(self, *banknotes: Banknote):
        self.container = []
        self.container.extend(banknotes)
        self.index = 0

    def __repr__(self):
        return f'Wallet({self.container})'

    def __contains__(self, item):
        return item in self.container

    def __bool__(self):
        return len(self.container) > 0

    def __len__(self):
        return len(self.container)

    def __call__(self):
        return f'{sum(map(lambda x: x.value, self.container))} $'

    def __iter__(self):
        return Iterator(self.container)

    def __getitem__(self, item: int):
        print("!!!")
        if item < 0 or item > len(self.container):
            raise IndexError
        return self.container[item]

    def __setitem__(self, key: int, value: Banknote):
        if key < 0 or key > len(self.container):
            raise IndexError
        self.container[key] = value


if __name__ == '__main__':
    banknote = Banknote(50)
    fifty = Banknote(50)
    hundred = Banknote(100)
    wallet = Wallet(fifty, hundred, hundred)
    wallet[0] = Banknote(500)

    for money in wallet:
        print(money)
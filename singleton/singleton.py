# Паттерны или шаблоны разработки - это общие способы решения частых задач и проблем
# Singleton Одиночка - это щаблон предоставления глобального доступа к состоянию,
# объект всегда один
# Monostate - это шаблон представления глобального доступа к состоянию,
# объекты могут быть разными
# нужен для одной точки доступа к ресурсу/данным и для того, чтобы ресурсоёмкие задачи
# сделать 1 раз

# Плюсы: 1 раз выполняем тяжёлые задачи, имеет 1 вход для всей системы
# Минусы: общесистемная глобальная переменная
# Модуль в Python - это singleton


class Singleton:
    instance = None

    def __new__(cls):
        if Singleton.instance is None:
            Singleton.instance = super().__new__(cls)
            Singleton._do_work(Singleton.instance)
        return Singleton.instance

    def _do_work(self):
        print('do some hard work')
        # parse, db, work with data/resources etc...
        self.data = 101


class Monostate:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        if not self._shared_state:
            print('do some hard work')
            # parse, db, work with data/resources etc...
            self.data = 101


if __name__ == '__main__':
    first = Monostate()
    print(first)
    second = Monostate()
    print(second)
    print(first is second)
    print(first.data)
    first.data = 102
    print(second.data)
    print(Monostate())


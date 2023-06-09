"""
dict - словарь, отображение, хеш-мап, ассоциативный массив, коллекция пар ключ-значение,
где ключом может быть только hashable тип, доступ по ключу и проверка наличия ключа O(1),
с питона 3.7 хранит порядок вставки
пустой словарь создавать лучше через {}, а не dict(), под капотом будет создано 8 элементов

hashable != Imutable
set - множество, хешсет, неупорядоченный набор hashable обЪектов, доступ и проверка наличия O(1)
frozenset - неизменяемый брат множества

Получем хеш -> высчитываем позицию ы массиве -> если элементанет, то жействуем соответственно задаче ->
есди элемент есть, то сравниваем ключ == тому сто ищем -> если ключ не равен искомому то ищем дополнительны бакет

По умолчанию самописные классы возвращают хэш основанный на id, если переопределяете хэш, то всег  проверяйте,
что у всех равных обЪектов одиноквый хеш.
Что можно положить в сет / словарь и проверка на содержимое
"""

from timeit import timeit

# x = timeit("dict()")
# y = timeit("{}")
#
# print(x)
# print(y)

# a_dict = dict(x=1, y=2, z=3)
# a_set = set('xyz')
# print(a_dict)
# print(a_set)

# a_set = {1, 2, 3, 4, 5, 1822763781, -38474773472382992929, 0}
# print(a_set)


# a_tuple = (1, 2, 3)
# a_set = {a_tuple}
# print(a_set)
# x = {a_tuple: "aaa"}
# print(x)



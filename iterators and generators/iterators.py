"""
Контейнер - это тип данных, который инкапсулирует в себя значения других типов

Итерабельный объект (в оригинальной терминологии - существительное "iterable") -
это и последовательности (списки, строки и т д), файлы, а также экземпляры любых
классов, в которых определён метод __iter__() или __getitem__()

Итерабельные объекты могут быть использованы внутри цикла for, а также во многих
других случаях, когда могут использованы внутри цикла for, а также во многих
других случаях, когда ожидается последовательность (функции sum, zip, map)

Когда итерабельный объект передаётся во встроенную функцию iter(), она
возвращает итератор для данного объекта, который позволяет один раз пройти
по значениям итерабельного объекта.

Итератор (iterator) - это объект, который представляет поток данных.
Повторяемые вызовы метода __next__() итератора или передача его встроенной
функции next() возвращает последующие элементы потока.

Если больше не осталось данных, выбрасывается исключение StopIteration.
После этого итератор исчерпан и любые последующие вызовы его метода __next__()
снова генерируют исключение Stopiteration.

Итераторы обязаны иметь метод __iter__, который возвращает сам объект итератора,
так что любой итератор также является итерабельным объектом и может быть
использован почти везде, где принимаются итерабельные объекты.
"""
import math

# def my_for(iterable, callback):
#     it = iter(iterable)
#     while True:
#         try:
#             value = next(it)
#             callback(value)
#         except StopIteration:
#             break
#
#
# def loop_body(value):
#     print(f'Next value received: {value}')
#
#
# my_for(range(10), loop_body)

# class SimpleIterator:
#     def __getitem__(self, index):
#         if 0 <= index <= 5:
#             return index * 2
#         else:
#             raise IndexError
#
#
# iterable = SimpleIterator()
# for value in iterable:
#     print(value)


class MyRange:
    def __init__(self, first, second=None, step=1):
        if second is None:
            self.start = 0
            self.end = first
        else:
            self.start = first
            self.end = second

        if step != 0:
            self.step = step
        else:
            raise ValueError('Step cannot be zero')

        self.length = math.ceil((self.end - self.start) / self.step)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if 0 <= index < len(self):
            return self.start + index * self.step
        else:
            raise IndexError('MyRange index out of range')

    def __iter__(self):
        return RangeIterator(self)

    def __repr__(self):
        return f'MyRange({self.start} {self.end} {self.step})'


class RangeIterator:
    def __init__(self, range_instance):
        self.range = range_instance
        self.next_value = range_instance.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_value >= self.range.end and self.range.step > 0 or \
                self.next_value <= self.range.end and self.range.step < 0:
            raise StopIteration

        result = self.next_value
        self.next_value += self.range.step

        return result

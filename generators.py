"""
Генераторы

Функция-генератор(generator function) - это функция, которая возвращает
специальный итератор генератора (generator iterator) (также объект-генератор - generator object).
Она характеризуется наличием ключевого слова yield внутри функции.

Термин генератор (generator), в зависимости от контекста, может означать либо
функцию - генератор, либо итератор генератора (чаще всего последнее).

Методы __iter__ и __next__ у генераторов создаются автоматически.

yield замораживает состояние функции - генератора и возвращает текущее значение.
После следующего вызова __next__() функция-генератор продолжает своё выполнение с того места,
где она была приостановлена.

Когда выполнение функции-генератора завершается (при помощи ключевого слова
return или достижиния конца функции), возникает исключение StopIteration.
"""


import re
string = "teSt1 test2 teSt3 test4 teSt5"
print(re.subn(r"s", "x", string, flags=re.IGNORECASE))
"""
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""


def is_simple(num: int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def simple_generate(number: int):
    i = 2
    yield i
    i += 1
    while i <= number:
        if is_simple(i):
            yield i
        i += 2


iter_gen = simple_generate(27)

for i in range(26):
    print(next(iter_gen))

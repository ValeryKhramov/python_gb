# Документация функции
"""Пояснения к однострочной строке документации
● Тройные кавычки используются, даже если строка помещается на одной
строке. Это позволяет легко расширить его позже.
● Закрывающие кавычки находятся на той же строке, что и открывающие. Это
выглядит лучше для однострочников.
● Нет пустой строки ни до, ни после строки документации.
● Строка документации — это фраза, заканчивающаяся точкой. Он описывает
действие функции или метода как команду
● Однострочная строка документации не должна повторять параметры
функции."""


def max_before_hundred(*args):
    """Return the maximum number not exceeding 100."""
    m = float('-inf')
    for item in args:
        if m < item < 100:
            m = item
    return m


print(max_before_hundred(-42, 73, 256, 0))


def max_before_hundred_1(*args):
    """Return the maximum number not exceeding 100.
    :param args: tuple of int or float numbers
    :return: int or float number from the tuple args
    """
    pass

help(max_before_hundred)
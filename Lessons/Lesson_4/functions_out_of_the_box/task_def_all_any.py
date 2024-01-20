# all(iterable)Функция возвращает истину, если все элементы последовательности являются истиной.


def all_(iterable):  # Своя реализация функции all
    for element in iterable:
        if not element:
            return False
    return True


numbers = [42, -73, 1024]
if all(map(lambda x: x > 0, numbers)):
    print('Все элементы положительные')
else:
    print('В последовательности есть отрицательные и/или нулевые элементы')


# any(iterable)Функция возвращает истину, если хотя бы один элемент последовательности являются истиной.


def any_(iterable):  # Своя реализация функции any
    for element in iterable:
        if element:
            return True
    return False


numbers = [42, -73, 1024]
if any(map(lambda x: x > 0, numbers)):
    print('Хотя бы один элемент положительный')
else:
    print('Все элементы не больше нуля')

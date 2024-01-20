# locals Функция возвращает словарь переменных из локальной области видимости на момент вызова функции.
SIZE = 10


def func(a, b, c):
    x = a + b
    print(locals())
    z = x + c
    return z


func(1, 2, 3)
print()

# globals Функция возвращает словарь переменных из глобальной области видимости, т.е. из пространства модуля.

SIZE = 10


def func(a, b, c):
    x = a + b
    print(globals())
    z = x + c
    return z


print(globals())
print(f'{func(1, 2, 3) = }')

# изменяем словарь globals
x = 42
glob_dict = globals()
glob_dict['x'] = 73
print(f'{x = }')
print()

# vars Функция без аргументов работает аналогично функции locals().
print(vars(int))

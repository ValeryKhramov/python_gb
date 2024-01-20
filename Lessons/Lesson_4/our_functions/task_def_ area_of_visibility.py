# Область видимости переменных

"""Локальная область видимости"""


def func(y: int) -> int:
    x = 100
    print(f'In func {x = }')  # Для демонстрации работы, но не для привычки принтить из функции
    return y + 1


print("Локальная область видимости")
x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')
print()

"""Глобальная область видимости"""


def func(y: int) -> int:
    global x
    x += 100
    print(f'In func {x = }')  # Для демонстрации работы, но не для привычки принтить из функции
    return y + 1


print("Глобальная область видимости")
x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')
print()

"""Не локальная область видимости"""


def main(a):
    x = 1

    def func(y):
        nonlocal x
        x += 100
        print(f'In func {x = }')  # Для демонстрации работы, но не для привычки принтить из функции
        return y + 1

    return x + func(a)


print("Не локальная область видимости")
x = 42
print(f'In main {x = }')
z = main(x)
print(f'{x = }\t{z = }')

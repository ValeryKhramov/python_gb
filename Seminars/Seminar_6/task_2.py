"""
 Создайте модуль с функцией внутри.
 Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
 Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
 Функция выводит подсказки “больше” и “меньше”.
 Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь"""
from random import randint


def guess(min_number: int, max_number: int = 10, count: int = 3) -> bool:
    print(f'Угадайте целое число в диапазоне {min_number} и {max_number}!')
    guess_number = randint(min_number, max_number)

    for i in range(count):
        number = int(input(f'Введите целое число: '))
        if number == guess_number:
            return True
        elif number > guess_number:
            print(f"Загаданное число меньше. Число оставшихся попыток: {count - i - 1}")

        elif number < guess_number:
            print(f'Загаданное число больше. Число оставшихся попыток: {count - i - 1}')

        else:
            return False


if __name__ == '__main__':
    print(guess(0, 10, 5))

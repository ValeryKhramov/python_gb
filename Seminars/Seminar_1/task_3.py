# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.


result = None

while True:
    number = int(input("Введите целое число в диапазоне от 1 до 999: "))
    if not 1 < number < 999:
        print("Число не входит в диапазон от 1 до 999.")
        continue

    if 0 < number < 10:
        result = number ** 2
    elif number < 100:
        result = (number % 10) * (number // 10)
    else:
        result = (number % 10 * 100) + (number // 10 % 10 * 10) + (number // 100)
    break

print(result)

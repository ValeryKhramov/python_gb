# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
number = int(input("Введите целое число N: "))
number_two = int(input("Введите целое число E: "))

summa = 0
for i in range(0, number + 1, 2):
    if i % number_two != 0:
        summa += i
print(f'Сумма четных чисел от 0 до числа N = {summa}')

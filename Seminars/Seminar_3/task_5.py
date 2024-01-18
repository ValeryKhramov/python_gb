# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

numbers = [1, 2, 3, 5, 7, 2, 5]
result = []
for i, elem in enumerate(numbers, 1):
    if elem % 2 != 0:
        result.append(i)

print(result)



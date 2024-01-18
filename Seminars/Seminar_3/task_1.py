# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.

# Короткое решение *set использует под капотом алгоритм сортировки для сравнения чисел
numbers = [1, 3, 5, 8, 9, 7, 1, 3]
un_numbers = list(set(numbers))
print(un_numbers)  # Линейная сложность

# Решение через цикл
uni_numbers = []
for number in numbers:
    if number not in uni_numbers:
        uni_numbers.append(number)
print(uni_numbers)  # Сложность O(n**2)

# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

numbers = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, ]

for i in set(numbers):
    counter = numbers.count(i)
    if counter > 1:
        for _ in range(counter):
            numbers.remove(i)
print(numbers)


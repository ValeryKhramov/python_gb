# Сортировка списка. Сортирует непосредственно переданный список в аргументах.

# Сортировка происходит по однотипным элементам
# my_list = ['H', 'e', 'l', 'l', 'o', 1, 3, 5, 7]
my_list = [45, 56, 856, 234, 567, 32, 12, 5, 8, 679, 345, 68, 345, 7089]
my_list.sort()  # TypeError: '<' not supported between instances of 'int' and 'str'
print(my_list)
res = sorted(my_list)  # TypeError: '<' not supported between instances of 'int' and 'str'


my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
"""
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""


def sum_of_numbers_between_indices(in_list: list[int | float],
                                   start_index: int,
                                   end_index: int) -> int | float:
    if start_index > end_index:
        start_index, end_index = end_index, start_index
    if end_index > len(in_list):
        end_index = len(in_list)
    if start_index < 0:
        start_index = 0
    return sum(in_list[start_index:end_index])


numbers = [1, 2, 3, 4, 5, 76, 77, 8, 9]
print(sum_of_numbers_between_indices(numbers, 0, 3))

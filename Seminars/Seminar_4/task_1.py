"""
✔ Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки."""


def string_parse(string: str) -> str:
    """
    Обрабатывает строку.
    :param string:
    :return:
    """
    lst = text.split()
    lst.sort()
    longest_word = len(max(lst, key=len))

    res = ''
    for i, elem in enumerate(lst, 1):
        res += f'{i}{elem:>{longest_word + 1}}\n'
    return res


text = "Строки нумеруются начиная с единицы."
print(string_parse(text))

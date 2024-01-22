"""
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""


def unicode_dictionary_generation(diapazon: str) -> dict[str, int]:
    result = {}
    start, end = map(int, diapazon.split())
    for i in range(min(start, end), max(start, end)):
        # result[chr(i)] = i
        result.setdefault(chr(i), i)
    return result


text = '97 123'
print(unicode_dictionary_generation(text))

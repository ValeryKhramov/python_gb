"""
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""


def generate_unicode_list(text: str) -> list[int]:
    result = set()
    for char in text:
        result.add(ord(char))
    return sorted(result, reverse=True)


text = ('Сформируйте список с уникальными кодами Unicode каждого '
        'символа введённой строки отсортированный по убыванию')
print(generate_unicode_list(text))

# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

text = 'Обратите внимание на порядок ключей.'
res = {}

for char in text:
    # res.setdefault(char, 0)
    # res[char] = res[char] + 1
    res[char] = res.get(char, 0) + 1
print(res)

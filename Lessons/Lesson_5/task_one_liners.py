# Полезные однострочники

# Обмен значений переменных местами
a = 42
b = 73
a, b = b, a
print(f'{a = }\t{b = }')

# Распаковка и упаковка коллекций
a, b, c = input("Три символа: ")
print(f'{a=} {b=} {c=}')

a, b, c = ("один", "два", "три",)
print(f'{a=} {b=} {c=}')

# Распаковка коллекции с упаковкой “лишнего”, упаковка со звёздочкой
data = ["один", "два", "три", "четыре", "пять", "шесть", "семь", ]
a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}')
a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}')
a, *b, c, d = data
print(f'{a=} {b=} {c=} {d=}')
*a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}')

link = 'https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'
prefix, *_, suffix = link.split('/')

# Распаковка со звёздочкой
data = [2, 4, 6, 8, 10, ]
for item in data:
    print(item, end='\t')

data = [2, 4, 6, 8, 10, ]
print(*data, sep='\t')

# Множественное присваивание

a = b = c = 0  # копирует не объект, а ссылку на него
a += 42
print(f'{a=} {b=} {c=}')

# map(function, iterable) — принимает на вход функцию и последовательность.
# Функция применяется к каждому элементу последовательности и возвращает map
# итератор.

texts = ["Привет", "ЗДОРОВА", "привеТствую"]
res = map(lambda x: x.lower(), texts)
print('map')
print(*res)  # распаковка объекта
print()

# filter(function, iterable) — принимает на вход функцию и последовательность. Если
# функция возвращает истину, элемент остаётся в последовательности. Как и map
# возвращает объект итератор.
numbers = [42, -73, 1024]
res = tuple(filter(lambda x: x > 0, numbers))
print('filter')
print(res)
print()

# zip(*iterables, strict=False) — принимает несколько последовательностей и
# итерируется по ним параллельно.

names = ["Иван", "Николай", "Пётр"]
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99]
print('zip')
for name, salary, award in zip(names, salaries, awards):
    print(f'{name} заработал {salary:.2f} денег и премию {salary * award:.2f}')

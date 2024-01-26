import random as rnd

START = -100
STOP = 1_000
STEP = 10
data = [2, 4, 6, 8, 42, 73]

print(rnd.random())
rnd.seed(42)
state = rnd.getstate()
print(rnd.random())
rnd.setstate(state)
print(rnd.random())

print(rnd.randint(START, STOP))
print(rnd.uniform(START, STOP))
print(rnd.choice(data))
print(rnd.randrange(START, STOP, STEP))

print(data)
rnd.shuffle(data)
print(data)

print(rnd.sample(data, 2))
print(rnd.sample(data, 2, counts=[1, 1, 1, 1, 1, 100]))

"""
● randint(a, b) — генерация случайного целого числа в диапазоне от a
включительно до b включительно — [a, b].
● uniform(a, b) — генерация случайного вещественного числа в диапазоне от a
до b. Правая граница может как входить, так и не входить в возвращаемый
диапазон. Зависит от способа округления.
● choice(seq) — возвращает случайный элемент из непустой
последовательности.
● randrange(stop) или randrange(start, stop[, step]) работает как вложение
функции range в функцию choice, т.е. choice(range(start, stop, step)).
Возвращает случайное число от start до stop с шагом step.
● shuffle(x) — перемешивает случайным образом изменяемую
последовательность in place, т.е. не создавая новую.
● sample(population, k, *, counts=None) — выбирает k уникальных элементов из
последовательности population и возвращает их в новой последовательности.
Параметр counts позволяет указать количество повторов элемента."""
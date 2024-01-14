# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой


import decimal
import math
PI = decimal.Decimal(math.pi)

diam = float(input("Введите диаметр круга: "))
decimal.getcontext().prec = 48

radius = decimal.Decimal(diam / 2)
area = PI * radius * radius
length = 2 * PI * radius
print(f'Площадь круга - {area}\n'
      f'Длина окружности - {length}')
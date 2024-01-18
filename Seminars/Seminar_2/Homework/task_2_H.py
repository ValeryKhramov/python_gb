# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.
from fractions import Fraction

frac1 = input('Введите первую дробь в виде "1/2": ')
frac2 = input('Введите вторую дробь в виде "1/2": ')

fract_1_elem = list(map(int, frac1.split('/')))
fract_2_elem = list(map(int, frac2.split('/')))

fract_1_check = Fraction(fract_1_elem[0], fract_1_elem[1])
fract_2_check = Fraction(fract_2_elem[0], fract_2_elem[1])

sum_of_fractions = (f'{fract_1_elem[0] * fract_2_elem[1] + fract_2_elem[0] * fract_1_elem[1]}/'
                    f'{fract_1_elem[1] * fract_2_elem[1]}')
product_of_fractions = f'{fract_1_elem[0] * fract_2_elem[0]}/{fract_1_elem[1] * fract_2_elem[1]}'

check_sum_of_fractions = fract_1_check + fract_2_check
check_product_of_fractions =  fract_1_check * fract_2_check

print(f'Сумма дробей: {sum_of_fractions}',
      f'Произведение дробей: {product_of_fractions}', sep='\n')
print(f'Сумма дробей: {check_sum_of_fractions}',
      f'Произведение дробей: {check_product_of_fractions}', sep='\n')

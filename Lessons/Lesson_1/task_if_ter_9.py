# Обычный if
my_math = int(input('2 + 2 = '))
if 2 + 2 == my_math:
    print('Верно!')
else:
    print('Вы уверены?')

# С помощью тернарного оператора
my_math = int(input('2 + 2 = '))
print('Верно!' if 2 + 2 == my_math else 'Вы уверены?')
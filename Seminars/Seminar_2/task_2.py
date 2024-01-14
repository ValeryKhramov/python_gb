# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление
number = int(input("Введите положительное целое число: "))
result = ""
res = ""
# В двоичную систему исчисления
print(bin(number))
while number != 0:
    result = str(number % 2) + result
    number //= 2

print(result)

# В восьмеричную систему исчисления
number = int(input("Введите положительное целое число: "))
print(oct(number))
while number != 0:
    res = str(number % 8) + res
    number //= 8

print(res)


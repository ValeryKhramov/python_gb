# Напишите программу, которая запрашивает год и проверяет его на високосность.
MAIN_CONDITION = 4
ADD_CONDITION = 100
YEAR_EXCEPTION = 400

year = int(input("Введите год в формате yyyy: "))


if (year % MAIN_CONDITION != 0 or year % ADD_CONDITION == 0
        and year % YEAR_EXCEPTION != 0):
    result = "Год обычный"
else:
    result = "Год високосный"
print(result)

DEFAULT = 42
num = int(input("Введите уровень или нольдля значения по умолчанию: "))
level = num or DEFAULT
print(level)
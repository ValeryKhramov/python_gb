number = input("Введите число: ")
if number.isdigit():
    number = int(number)
    print(bin(number), oct(number), hex(number), sep='\n')
elif number.isascii():
    print("Текст написан в ASCII")

# Срезы в строке
text = 'Hello world!'
print(text[6])
print(text[3:7])

# Замена элемента в строке с созданием новой строки(Строка неизменяемый тип данных)
new_txt = text.replace('l', 'L', 2)
print(text, new_txt, sep='\n')

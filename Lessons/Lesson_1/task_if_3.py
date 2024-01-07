pwd = 'text' # else - иначе
res = input('Input password: ')
if res == pwd:
    print('Доступ разрешён')
    print('Но будьте осторожны')
else:
    print('Доступ запрещён')
print('Работа завершена')
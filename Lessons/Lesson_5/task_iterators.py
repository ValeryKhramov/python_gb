# Итераторы
import functools
# Функция iter(object[, sentinel]).
data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)


f = open('mydata.bin', 'rb')
for block in iter(functools.partial(f.read, 16), b''):
    print(block)
f.close()

# Функция next(iterator[, default])
data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter, 'stop iteration'))

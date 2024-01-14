# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
import sys
from typing import Hashable

data = [1, 2.0, '3', [4], (5,)]
for n, obj in enumerate(data, 0):
    print(f'{n} - {obj} - {id(obj)} - {sys.getsizeof(obj)} '
          f'{hash(obj) if isinstance(obj, Hashable) else "Объект нехэшируемый"} '
          f'{"Число целое" if isinstance(obj, int) else ""} '
          f'{"Строка" if isinstance(obj, str) else ""} ')


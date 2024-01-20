# Позиционные и ключевые параметры
def func(positional_only_parameters, /, positional_or_keyword_parameters, *, keyword_only_parameters):
    pass


def standard_arg(arg):
    """Пример обычной функции"""
    print(arg)  # Принтим для примера, а не для привычки


standard_arg(42)
standard_arg(arg=42)


def pos_only_arg(arg, /):
    """Пример только позиционной функции:"""
    print(arg)  # Принтим для примера, а не для привычки


pos_only_arg(42)


# pos_only_arg(arg=42)  # TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'


def kwd_only_arg(*, arg):
    """Пример только ключевой функции"""
    print(arg)  # Принтим для примера, а не для привычки


# kwd_only_arg(42)
kwd_only_arg(arg=42)


def combined_example(pos_only, /, standard, *, kwd_only):
    """Пример функции со всеми вариантами параметров:"""
    print(pos_only, standard, kwd_only)  # Принтим для примера, а не для привычки


# combined_example(1, 2, 3)  # TypeError: combined_example() takes 2 positional arguments but 3 were given
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)


# combined_example(pos_only=1, standard=2, kwd_only=3)  # TypeError: combined_example() got some positional-only arguments
# passed as keyword arguments: 'pos_only'

# Параметры *args и **kwargs

def mean(args):
    return sum(args) / len(args)


print(mean([1, 2, 3]))


# print(mean(1, 2, 3))  # TypeError: mean() takes 1 positional argument but 3 were given


def mean(*args): # Функция принимает любое число позиционных аргументов и переводит их в кортеж
    return sum(args) / len(args)


print(mean(*[1, 2, 3]))
print(mean(1, 2, 3))


def school_print(**kwargs): # Функция работает с любым количеством ключевых аргументов и переводит их в словарь
    for key, value in kwargs.items():
        print(f'По предмету "{key}" получена оценка {value}')


school_print(химия=5, физика=4, математика=5, физра=5)

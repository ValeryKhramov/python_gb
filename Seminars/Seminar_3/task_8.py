# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

friends = {
    'Афанасий': ('аккордеон', 'баян', 'велосипед', 'настроение'),
    'Борис': ('аккордеон', 'баян', 'велосипед', 'настроение'),
    'Владимир': ('аккордеон', 'баян', 'велосипед', 'розетка', 'бритва'),
    }

all_things = []
for things in friends.values():
    all_things.extend(things)

all_things_unit = set(all_things)
# print(all_things_unit)
)
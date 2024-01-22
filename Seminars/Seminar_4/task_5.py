"""
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
"""


def premium_calculation(names: list[str], rate: list[int], bonus: list[str]) -> dict[str, float]:
    result = {}
    for i in range(len(names)):
        result.setdefault(names[i], round(rate[i] * float(bonus[i].replace('%', '')) // 100, 2))
    return result


def premium_calculation_zip(names: list[str], rate: list[int], bonus: list[str]) -> dict[str, float]:
    res = {}
    for name, salery, bonus in zip(names, rate, bonus):
        res[name] = round(salery * float(bonus.replace('%', '')) // 100, 2)
    return res


if __name__ == '__main__':
    names = ['Python', 'Rust', 'Java']
    rate = [100, 137, 89]
    bonus = ['10.4%', '10.0%', '12.5%']
    result = premium_calculation(names, rate, bonus)
    result_zip = premium_calculation_zip(names, rate, bonus)
    print(result, result_zip, sep='\n')

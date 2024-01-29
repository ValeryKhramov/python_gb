from datetime import datetime

MONTHS = {
    1: range(1, 32),
    2: range(1, 29),
    3: range(1, 32),
    4: range(1, 31),
    5: range(1, 32),
    6: range(1, 31),
    7: range(1, 32),
    8: range(1, 32),
    9: range(1, 31),
    10: range(1, 32),
    11: range(1, 31),
    12: range(1, 32),
}


def parse_data(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    return _is_valid_year(year) and _is_valid_month(month) and _is_valid_day(day, month, year)


def _is_valid_day(day: int, month: int, year: int) -> bool:
    if _is_leap_year(year) and month == 2:
        return day in range(1, 30)
    return day in MONTHS[month]


def _is_valid_month(month: int) -> bool:
    return month in range(1, 13)


def _is_valid_year(year: int) -> bool:
    return year in range(1, 10_000)


def _is_leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

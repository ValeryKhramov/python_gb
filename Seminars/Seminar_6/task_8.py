"""
 Создайте пакет с всеми модулями, которые вы создали за
время занятия.
 Добавьте в __init__ пакета имена модулей внутри дандер
__all__.
 В модулях создайте дандер __all__ и укажите только те
функции, которые могут верно работать за пределами
модуля."""
# * - на уровне пакета
from new_package import *
# * - на уровне модуля в пакете
from new_package.data_parser import *

data_parser.parse_data('')
parse_data('')

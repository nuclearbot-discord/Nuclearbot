from requests import get

from modules.bot_funcs.for_funcs import *
from modules.config import settings

def get_next (message, command):
    command_all = settings ['prefix'] + command.lower () + ' '
    return command_all.join (message.content.lower().split (command_all) [1:])

def all_digits (msg):
    int_str = ''

    for char in msg:
        if char.isdigit ():
            int_str += char

    return int (int_str)
def all_digits2 (msg):
    int_str = ''

    for char in msg:
        if char.isdigit ():
            int_str += char

    return int_str
async def mat(message, stroka):
    import string

    words = ["банан", "помидор"]

    print("Фильтруемые слова:", words)

    # Фраза, которую будем проверять.
    phrase = stroka

    def distance(a, b):
        "Calculates the                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   distance between a and b."
        n, m = len(a), len(b)
        if n > m:
            # Make sure n <= m, to use O(min(n, m)) space
            a, b = b, a
            n, m = m, n

        current_row = range(n + 1)  # Keep current and previous row, not entire matrix
        for i in range(1, m + 1):
            previous_row, current_row = current_row, [i] + [0] * n
            for j in range(1, n + 1):
                add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
                if a[j - 1] != b[i - 1]:
                    change += 1
                current_row[j] = min(add, delete, change)

        return current_row[n]

    d = {'а': ['а', 'a', '@'],
         'б': ['б', '6', 'b'],
         'в': ['в', 'b', 'v'],
         'г': ['г', 'r', 'g'],
         'д': ['д', 'd'],
         'е': ['е', 'e'],
         'ё': ['ё', 'e'],
         'ж': ['ж', 'zh', '*'],
         'з': ['з', '3', 'z'],
         'и': ['и', 'u', 'i'],
         'й': ['й', 'u', 'i'],
         'к': ['к', 'k', 'i{', '|{'],
         'л': ['л', 'l', 'ji'],
         'м': ['м', 'm'],
         'н': ['н', 'h', 'n'],
         'о': ['о', 'o', '0'],
         'п': ['п', 'n', 'p'],
         'р': ['р', 'r', 'p'],
         'с': ['с', 'c', 's'],
         'т': ['т', 'm', 't'],
         'у': ['у', 'y', 'u'],
         'ф': ['ф', 'f'],
         'х': ['х', 'x', 'h', '}{'],
         'ц': ['ц', 'c', 'u,'],
         'ч': ['ч', 'ch'],
         'ш': ['ш', 'sh'],
         'щ': ['щ', 'sch'],
         'ь': ['ь', 'b'],
         'ы': ['ы', 'bi'],
         'ъ': ['ъ'],
         'э': ['э', 'e'],
         'ю': ['ю', 'io'],
         'я': ['я', 'ya']
         }

    for key, value in d.items():
        # Проходимся по каждой букве в значении словаря. То есть по вот этим спискам ['а', 'a', '@'].
        for letter in value:
            # Проходимся по каждой букве в нашей фразе.
            for phr in phrase:
                # Если буква совпадает с буквой в нашем списке.
                if letter == phr:
                    # Заменяем эту букву на ключ словаря.
                    phrase = phrase.replace(phr, key)

    # Проходимся по всем словам.
    for word in words:
        # Разбиваем слово на части, и проходимся по ним.
        for part in range(len(phrase)):
            # Вот сам наш фрагмент.
            fragment = phrase[part: part + len(word)]
            # Если отличие этого фрагмента меньше или равно 25% этого слова, то считаем, что они равны.
            if distance(fragment, word) <= len(word) * 0.25:
                # Если они равны, выводим надпись о их нахождении.
                await message.channel.send(f"Найдено {word}\nПохоже на {fragment}")
__all__ = ['get_next', 'all_digits']
__ver__ = '0.2'

add_module (__name__, __ver__)

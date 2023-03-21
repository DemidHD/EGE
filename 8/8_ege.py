"""
Все 5-буквенные слова, составленные из букв А, О, У, записаны в алфавитном порядке. Вот начало списка:
1.ААААА
2.ААААО
3.ААААУ
4.АААОА
...
Укажите номер первого слова, которое начинается с буквы О.
"""

from itertools import product

k = 0

for num in product('АОУ', repeat=5):
    word = ''.join(num)
    k += 1
    if word[0] == 'О':
        print(k, word)
        break

"""
Все 6-буквенные слова, составленные из букв С, В, Е, Т, записаны в алфавитном порядке и пронумерованы.Вот начало списка:
1.ВВВВВB
2.ВВВВВЕ
3.ВВВВВС
4.ВВВВВТ
5.ВВВВЕВ
...
Под каким номером стоит первое из слов, которое начинается с буквы Т?
"""

from itertools import product

k = 0

for num in product('ВЕСТ', repeat=6):
    word = ''.join(num)
    k += 1
    if word[0] == 'Т':
        print(k, word)
        break
from itertools import product
"""8"""
k = 0
for i in product('ЕКОР', repeat=6):
    lit = ''.join(i)
    k += 1
    if lit[0] == 'О' and 'ОЕ' not in lit:
        print(k, lit)
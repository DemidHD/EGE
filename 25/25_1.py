"""
Среди целых чисел, принадлежащих числовому отрезку [268312;336492], найдите числа,
которые представляют собой произведение двух различных простых делителей. Запишите в
ответе количество таких чисел и минимальное из них.
"""

result = []


def IsPrime(number):
    flag = 0
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            flag = 1
            break
    return flag == 0


for j in range(268312, 336493):
    t = 0
    for k in range(2, int(j ** 0.5)):
        if (j % k == 0) and IsPrime(k) and IsPrime(j // k):
            t = 1
            break
    if t == 1:
        result.append(j)

print(len(result), min(result))



"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""


def ls_min(query):  # Линейная сложность
    num = int(query[0])
    for i in range(1, len(query)):
        if num > int(query[i]):
            num = int(query[i])
    return num


query = input('ведите числа через пробел: ').rstrip()
result = ls_min(query.split(' '))
print(result)


def ls_min2(query):  # Квадратичная сложность
    for i in range(len(query)):
        for j in range(len(query)):
            if int(query[i]) <= int(query[j]):
                query[i], query[j] = query[j], query[i]

    return query[0]


query = input('ведите числа через пробел: ').rstrip()
result = ls_min2(query.split(' '))
print(result)
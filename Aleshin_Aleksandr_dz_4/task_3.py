"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

"""
Самые быстрые решения связаны со строками, так как в них нет маткматических операций и масих по себе операций меньше 
"""
from timeit import timeit

num = 100


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers(enter_num, revers_num)


print(
    timeit(
        "revers(num)",
        setup='from __main__ import revers, num',
        number=10000))


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


print(
    timeit(
        "revers_2(num)",
        setup='from __main__ import revers_2, num',
        number=10000))


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print(
    timeit(
        "revers_3(num)",
        setup='from __main__ import revers_3, num',
        number=10000))


def revers_4(enter_num):
    ls = []
    for i in str(enter_num):
        ls.insert(0,i)
    return ls

print(
    timeit(
        "revers_4(num)",
        setup='from __main__ import revers_4, num',
        number=10000))
print()
print(revers(num))
print(revers_2(num))
print(revers_3(num))
print(revers_4(num))
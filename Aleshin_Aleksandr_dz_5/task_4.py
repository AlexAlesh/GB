"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from timeit import timeit
from collections import OrderedDict

or_dict = OrderedDict()
no_or_dict = {}


def or_dict1(num):
    for i in range(10**3):
        or_dict[i] = i+1
    return num


print(timeit(
        'or_dict1(or_dict)',
        setup='from __main__ import or_dict1, or_dict',
        number=1000))


def no_or_dict1(num):
    for i in range(10**3):
        no_or_dict[i] = i+1
    return num


print(timeit(
        'no_or_dict1(no_or_dict)',
        setup='from __main__ import no_or_dict1, no_or_dict',
        number=1000))

or_dict1(or_dict)
no_or_dict1(no_or_dict)
# 2 test
test_or_dict = or_dict1(or_dict)
test_no_or_dict = no_or_dict1(no_or_dict)

def get_or(test):
    for i in range(10**2):
        test.get(i)
    return test


print(timeit(
        'get_or(test_or_dict)',
        setup='from __main__ import get_or, test_or_dict',
        number=1000))


def get_no_or(test):
    for i in range(10**2):
        test.get(i)
    return test


print(timeit(
        'get_no_or(test_or_dict)',
        setup='from __main__ import get_no_or, test_or_dict',
        number=1000))

get_no_or(test_no_or_dict)
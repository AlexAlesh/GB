# Алгоритмы и структуры данных на Python. Базовый курс Урок 5, Задание 3.

from memory_profiler import memory_usage
from collections import deque
import numpy


def memory(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper


lst = [i for i in range(1000)]
deq_lst = deque(lst)


@memory
def append_lst(lst):  # Выполнение заняло 4.1484375 Mib
    for i in range(100000):
        lst.append(i)
    return lst


@memory  # Выполнение заняло 3.66796875 Mib
def append_deq_lst(deq_lst):
    for i in range(100000):
        deq_lst.append(i)
    return deq_lst


append_lst(lst)
append_deq_lst(deq_lst)


@memory  # Выполнение заняло 1.55078125 Mib
def append_lst_1(lst):
    res = numpy.array(lst)
    res_2 = numpy.append(res, res + 1)
    return res_2


@memory  # Выполнение заняло 0.7890625 Mib
def append_deq_lst_1(deq_lst):
    res = numpy.array(deq_lst)
    res_2 = numpy.append(res, res + 1)
    return res_2


append_lst_1(lst)
append_deq_lst_1(deq_lst)


# Для оптимизации двух функции на добавление элементов в списке был тспользован модуль NumPy
# Проведение оптимизации имеет положительный эффект, так как  показатели затраченной памяти уменьшились.
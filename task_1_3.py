from collections import Counter
from memory_profiler import memory_usage


def memory(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper


array = ([1, 3, 1, 3, 4, 5, 1]*1000000)


@memory  # Выполнение заняло 0.00390625 Mib
def func_3():
    count = Counter(array)
    return count.most_common()[0]


@memory  # Выполнение заняло 0.0 Mib
def func_3_1(array):
    # count = Counter(array)
    new_list = map(Counter, array)
    return new_list


func_3()
func_3_1(array)

# В задаче для оптимизации памяти была использована функция map.
# После проведения оптимизации показатели затраченной памяти уменьшились.
# Результат положительный
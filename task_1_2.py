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


@memory  # Выполнение заняло 0.77734375 Mib
def revers_4(list_of_nums):
    return ''.join(reversed(str(list_of_nums)))


@memory  # Выполнение заняло 0.0 Mib
def revers_4_1(list_of_nums):
    yield reversed(str(list_of_nums))


list_of_nums = ('123456789' * 10000)
# for i in list_of_nums:
#     print(list_of_nums)

revers_4(list_of_nums)
revers_4_1(list_of_nums)

#  При оптимизации в этой задаче я использовал оператор yield, тем самым исключил возможность сохранения промежуточных
# результатов и всей последовательности в памяти. Как результат, оптимизиция прошла успешно.
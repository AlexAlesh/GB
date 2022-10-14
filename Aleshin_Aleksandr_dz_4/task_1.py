"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit

ls = [1,2,4,5,6,78,9,4,5,6,542,54,9,8,2,4,5,6,78,9,4,5,6,542,54,9,8]


def func_1(nums):

    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(func_1(ls))
print(timeit(
        'func_1(ls)',
        setup='from __main__ import func_1, ls',
        number=10000))

"""
Выполнение функции происходит в листкомприкейшин, что облегчает выполнение программы 
"""
def func_2(nums):

    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


print(func_2(ls))
print(timeit(
        'func_2(ls)',
        setup='from __main__ import func_2, ls',
        number=10000))

"""
Выполнение функции происходит в герераторе, так как он записает выражение в память и делает сброс,
это самое быстрое решение  
"""
def func_3(nums):
    return (i for i in range(len(nums)) if nums[i] % 2 == 0)


print(*func_3(ls))

print(timeit(
        'func_3(ls)',
        setup='from __main__ import func_3, ls',
        number=10000))

"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""
import collections, functools


def calculator():

    nums = collections.defaultdict(list)
    for i in range(1, 3):
        num = input(f'Введите {i} число: ')
        nums[i] = list(num)

    sum_16 = 0
    pro_16 = []
    for a in nums.values():
        sum_16 += int(''.join(a), 16)
        pro_16.append(int(''.join(a), 16))
    pro_16 = functools.reduce(lambda a,d: a*d, pro_16)
    print(f'Числа: {nums}')
    print(f'Сумма: {list(hex(sum_16).upper()[2:])}')
    print(f'Произведение: {list(hex(pro_16).upper()[2:])}')


calculator()

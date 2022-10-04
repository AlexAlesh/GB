"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def sum_num(count, num=0):

    if count != 1:
        if count > 0 and num == 0:
            num = count
            num = num / 2
            count -= 1
            return sum_num(count, num)
        else:
            num = num / 2
            count -= 1
            return sum_num(count, num)
    return num


count = float(input('Введите количество элементов: '))
print(sum_num(count))




"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

from timeit import timeit
from collections import deque

"""
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
"""

ls_num = [i for i in range(10**3)]
deque_num = deque([i for i in range(10**5)])
num = 10**4


print('append')
def ls_app(ls_num,num):
        for i in range(num):
                ls_num.append(i)
        return ls_num


ls_app(ls_num, num)
print(timeit(
        'ls_app(ls_num, num)',
        setup='from __main__ import ls_app, ls_num, num',
        number=1000))


def deque_app(deque_num,num):
        for i in range(num):
                deque_num.append(i)
        return deque_num


deque_app(deque_num,num)
print(timeit(
        'deque_app(deque_num,num)',
        setup='from __main__ import deque_app, deque_num,num',
        number=1000))


print('pop')
def ls_app(ls_num,num):
        for i in range(num):
                ls_num.pop()
        return ls_num


ls_app(ls_num, num)
print(timeit(
        'ls_app(ls_num, num)',
        setup='from __main__ import ls_app, ls_num, num',
        number=1000))


def deque_app(deque_num,num):
        for i in range(num):
                deque_num.pop()
        return deque_num


deque_app(deque_num,num)
print(timeit(
        'deque_app(deque_num,num)',
        setup='from __main__ import deque_app, deque_num,num',
        number=1000))


print('extend')
def ls_app(ls_num,num):
        for i in range(num):
                ls_num.extend('i')
        return ls_num


ls_app(ls_num, num)
print(timeit(
        'ls_app(ls_num, num)',
        setup='from __main__ import ls_app, ls_num, num',
        number=1000))


def deque_app(deque_num,num):
        for i in range(num):
                deque_num.extend('i')
        return deque_num


deque_app(deque_num,num)
print(timeit(
        'deque_app(deque_num,num)',
        setup='from __main__ import deque_app, deque_num,num',
        number=1000))


"""
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
"""

ls_num = [i for i in range(10**3)]
deque_num = deque([i for i in range(10**3)])
num = 10**2


print('appendleft')
def ls_app(ls_num,num):
        for i in range(num):
                ls_num.append(i)
        return ls_num


ls_app(ls_num, num)
print(timeit(
        'ls_app(ls_num, num)',
        setup='from __main__ import ls_app, ls_num, num',
        number=1000))


def deque_app(deque_num,num):
        for i in range(num):
                deque_num.appendleft(i)
        return deque_num


deque_app(deque_num,num)
print(timeit(
        'deque_app(deque_num,num)',
        setup='from __main__ import deque_app, deque_num,num',
        number=1000))


print('popleft')
def ls_app(ls_num,num):
        for i in range(num):
                ls_num.pop(i)
        return ls_num


ls_app(ls_num, num)
print(timeit(
        'ls_app(ls_num, num)',
        setup='from __main__ import ls_app, ls_num, num',
        number=1000))


def deque_app(deque_num,num):
        for i in range(num):
                deque_num.popleft()
        return deque_num


deque_app(deque_num,num)
print(timeit(
        'deque_app(deque_num,num)',
        setup='from __main__ import deque_app, deque_num,num',
        number=1000))


print('extendleft')
def ls_app(ls_num,num):
        for i in range(num):
                ls_num.extend('i')
        return ls_num


ls_app(ls_num, num)
print(timeit(
        'ls_app(ls_num, num)',
        setup='from __main__ import ls_app, ls_num, num',
        number=1000))


def deque_app(deque_num,num):
        for i in range(num):
                deque_num.extendleft('i')
        return deque_num


deque_app(deque_num,num)
print(timeit(
        'deque_app(deque_num,num)',
        setup='from __main__ import deque_app, deque_num,num',
        number=1000))


"""
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
"""


print('Замена элемента')
def ls_app(ls_num,num):
        for i in range(num):
                ls_num[i] = i-1
        return ls_num


ls_app(ls_num, num)
print(timeit(
        'ls_app(ls_num, num)',
        setup='from __main__ import ls_app, ls_num, num',
        number=1000))


def deque_app(deque_num,num):
        for i in range(num):
                deque_num[i] = i-1
        return deque_num


deque_app(deque_num,num)
print(timeit(
        'deque_app(deque_num,num)',
        setup='from __main__ import deque_app, deque_num,num',
        number=1000))


"""
В целом deque и списки очень близи по замеру временни, 
только при работе с popleft - deque сильно опережает списки
"""
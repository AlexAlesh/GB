import sys
from time import perf_counter
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []

print('Тест №1')
start = perf_counter()
for i in range(1, len(src)):
    if src[i] > src[i - 1]:
        result.append(src[i])
print(result, perf_counter() - start)
print(type(result), sys.getsizeof(result))

print('Тест №2')
start = perf_counter()
test_1 = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]
print(*test_1, perf_counter() - start)
print(type(test_1), sys.getsizeof(test_1))

print('Тест №3')
start = perf_counter()
test_2 = (src[i] for i in range(1, len(src)) if src[i] > src[i - 1])
print(*test_2, perf_counter() - start)
print(type(test_2), sys.getsizeof(test_2))

print('Тест №4')
start = perf_counter()


def test3(num):
    for i in range(1, len(src)):
        if src[i] > src[i - 1]:
           yield src[i]


print(*test3(src), perf_counter() - start)
print(type(test3(src)), sys.getsizeof(test3(src)))


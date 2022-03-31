def nums_generator(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


num_next = nums_generator(20)
print(next(num_next))
print(next(num_next))
print(next(num_next))
print(next(num_next))
print(*nums_generator(20))


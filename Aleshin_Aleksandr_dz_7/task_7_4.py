import os

final = {}
count = 1
buffer = []
for root, dirs, files in os.walk('./'):
    for file in files:
        root_f = os.path.join(root, file)
        len_size = os.stat(root_f).st_size
        buffer.append(len(str(len_size)))

for key in range(max(buffer)):
    count *= 10
    final[count] = 0
for num in buffer:
    final[10 ** num] += 1
print(final)

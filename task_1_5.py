# Алгоритмы и структуры данных на Python. Базовый курс Урок 1, Задание 5.
from pympler import asizeof


def sep():
    print('_' * 50)


class PlatesStack:
    def __init__(self, max_plates):
        self.plates = [[]]
        self.max_plates = max_plates

    def __str__(self):
        return str(self.plates)

    def is_empty(self):
        return self.plates == [[]]

    def push_in(self, items):
        if len(self.plates[len(self.plates) - 1]) < self.max_plates:
            self.plates[len(self.plates) - 1].append(items)
        else:
            self.plates.append([])
            self.plates[len(self.plates) - 1].append(items)

    def pop_out(self):
        res = self.plates[len(self.plates) - 1].pop()
        if len(self.plates[len(self.plates) - 1]) == 0:
            self.plates.pop()
        return res

    def get_val(self):
        return self.plates[len(self.plates) - 1]

    def stack_size(self):
        plates_count = 0
        for stack in self.plates:
            plates_count += len(stack)
            return len(self.plates)

    def stack_count(self):
        return len(self.plates)


p = PlatesStack(7)
print(asizeof.asizeof(p))
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
print(p)
print(asizeof.asizeof(p))
"""
424
[['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-']]
664
"""

sep()


class PlatesStack:
    __slots__ = ['plates', 'max_plates']

    def __init__(self, max_plates):
        self.plates = [[]]
        self.max_plates = max_plates

    def __str__(self):
        return str(self.plates)

    def is_empty(self):
        return self.plates == [[]]

    def push_in(self, items):
        if len(self.plates[len(self.plates) - 1]) < self.max_plates:
            self.plates[len(self.plates) - 1].append(items)
        else:
            self.plates.append([])
            self.plates[len(self.plates) - 1].append(items)

    def pop_out(self):
        res = self.plates[len(self.plates) - 1].pop()
        if len(self.plates[len(self.plates) - 1]) == 0:
            self.plates.pop()
        return res

    def get_val(self):
        return self.plates[len(self.plates) - 1]

    def stack_size(self):
        plates_count = 0
        for stack in self.plates:
            plates_count += len(stack)
            return len(self.plates)

    def stack_count(self):
        return len(self.plates)


p = PlatesStack(7)
print(asizeof.asizeof(p))
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
p.push_in('-')
print(p)
print(asizeof.asizeof(p))

"""
200
[['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-']]
440
"""

# В данной задаче я использовал оптимизацию за счет конструкции __slots__,
# что позволило снизить объём памяти, потребляемой экземплярами класса
# Оптимизиция прошла успешно, показатели используемой памяти уменьшились

class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        whole = self.nums // rows
        remainder = self.nums % rows
        qwe = ''
        for i in range(whole):
            w = '*' * rows + '\n'
            qwe += w
        return qwe + remainder * '*'


    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return 'Сложение ' + str(self.nums + other.nums)

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'Ячеек в первой клетке меньше или равно второй, вычитание невозможно'

    def __mul__(self, other):
        return 'Умножение ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'Деление ' + str(round(self.nums / other.nums))


cell_1 = Cell(5)
cell_2 = Cell(20)
print(cell_1)
print(cell_1 + cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(7))

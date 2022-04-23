class Matrix:
    def __init__(self, mat):
        self.mat = mat
        # print(self.mat)

    def __str__(self):
        mat_str = ''
        for ls in self.mat:
            mat_str += str(ls[0])
            mat_str += ' '
            mat_str += str(ls[1])
            mat_str += '\n'
        return mat_str

    def __add__(self, other):
        # print(self)
        # print(other)
        mat = []
        for line_1, line_2 in zip(self.mat, other.mat):
            for mat_1, mat_2 in zip(line_1, line_2):
                sum = mat_1 + mat_2
                mat.append(sum)
        return mat


matrix_1 = Matrix([[3, 2], [1, 4], [5, 9], [7, 8]])
matrix_2 = Matrix([[2, 1], [7, 5], [6, 7], [10, 9]])
print(matrix_1)
print(matrix_1 + matrix_2)

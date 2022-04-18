class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt(self):
        calculation = int(self._length * self._width * 25 * 5 / 1000)
        return f'Масса асфальта {calculation} T'


a = Road(20, 5000)
print(a.asphalt())



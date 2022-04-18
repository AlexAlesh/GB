
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Инструмент')


class Pen(Stationery):
    def draw(self):
        print('Ручка')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш')


class Handle(Stationery):
    def draw(self):
        print('Маркер')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()
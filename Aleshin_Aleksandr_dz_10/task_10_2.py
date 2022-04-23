from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def title(self):
        pass

    def __init__(self, size):
        self.size = size


class Coat(Clothes):
    def title(self):
        name = 'Пальто'
        return name

    def coat(self):
        V = self.size / 6.5 + 0.5
        return V

    @property
    def my_method(self):
        return f"Параметры, переданные в класс: {self.size}"


class Suit(Clothes):
    def title(self):
        name = 'Костюм'
        return name

    def suit(self):
        H = 2 * self.size + 0.3
        return H

    @property
    def my_method(self):
        return f"Параметры, переданные в класс: {self.size}"


coat = Coat(48)
suit = Suit(175)
print(f'{coat.title()} - {coat.coat()}. {coat.my_method}')
print(f'{suit.title()} - {suit.suit()}. {suit.my_method}')

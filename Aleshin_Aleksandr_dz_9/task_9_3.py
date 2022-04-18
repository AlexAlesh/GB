class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']  # ключ по которому будет заноситься зп
        self._income_bonus = income['bonus']


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'  # Ф.И и должность

    def get_total_income(self):
        return self._income_wage + self._income_bonus  # зп + премия


final = Position('Алешин', 'Александр', 'Сисадмин', {"wage": 45000, "bonus": 10000})
print(final.get_full_name())
print(final.get_total_income())
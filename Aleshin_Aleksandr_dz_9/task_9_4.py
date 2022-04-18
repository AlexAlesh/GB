class Car:
    def __init__(self, speed, color, name, police):
        self.speed = speed
        self.color = color
        self.name = name
        self.police = police

    def go(self):
        print(f'{self.name} Поехала')

    def stop(self):
        print(f'{self.name} Остановилась')

    def turn(self, direction):
        print(f'{self.name} направляется {direction}!')

    def show_speed(self):
        print('Скорость:', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Скорость:', self.speed)
        if self.speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    pass


sport_car = SportCar(240, 'Синий', 'Спорткар', False)
town_car = TownCar(140, 'Белая', 'Гражданский', False)
work_car = WorkCar(90, 'Красный', 'Пожарные', False)
police_car = PoliceCar(210, 'Черный', 'Полиция', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('прямо')
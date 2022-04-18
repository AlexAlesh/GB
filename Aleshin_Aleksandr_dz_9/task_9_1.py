import time


class TrafficLight:
    __color = (('красный', 7 ), ('жёлтый', 3), ('зелёный', 3))

    def running(self):
        while True:
            for i in TrafficLight.__color:
                print(i[0])
                time.sleep(i[1])


a = TrafficLight()
a.running()

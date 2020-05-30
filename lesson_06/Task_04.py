#   4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#      А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#      Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
#      текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
#      выводиться сообщение о превышении скорости.
#      Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
#      Выполните вызов методов и также покажите результат.
from random import randint


class Car:
    def __init__(self, name, color, is_police: bool):
        self.name = name
        self.speed = 0
        self.color = color
        self.is_police = is_police

    def go(self):
        print(self.name, ' поехала')
        self.speed = randint(20, 100)

    def stop(self):
        print(self.name, ' остановилась')
        self.speed = 0

    def turn(self, direction):
        if direction == 0:
            print(self.name, 'повернула на север')
        if direction == 1:
            print(self.name, 'повернула на юг')
        if direction == 2:
            print(self.name, 'повернула на запад')
        if direction == 3:
            print(self.name, 'повернула на восток')

    def show_speed(self):
        print('Скорость', self.name, ' = ', self.speed, '       Цвет: ', self.color, ' Это полиция? ', self.is_police)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышена скорость 60 ')
        return super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышена скорость 40: ')
        return super().show_speed()


class PoliceCar(Car):
    def __init__(self, *args, **kworgs):
        super().__init__(is_police=True, *args, **kworgs)


class SportCar(Car):
    def __init__(self, *args, **kworgs):
        super().__init__(is_police=False, *args, **kworgs)


cars = {}
cars['Ferrari'] = SportCar(name='Ferrari', color='red')
cars['Bus'] = WorkCar(name='Ekarus', color='orange', is_police=False)
cars['Ford'] = TownCar(name='Ford', color='black', is_police=False)
cars['Granta'] = PoliceCar(name='LadaGranta police', color='white/blue')


for key, car in cars.items():
    print("=" * 80)
    car.go()
    car.show_speed()
    car.turn(randint(0, 3))
    car.speed = 90
    car.show_speed()
    car.stop()
    car.show_speed()
    car.go()
    car.show_speed()
print("=" * 80)
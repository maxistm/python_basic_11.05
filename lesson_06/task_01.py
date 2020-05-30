# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
#    Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
#    Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
#    Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
#    Проверить работу примера, создав экземпляр и вызвав описанный метод.
#    Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time

class TrafficLight:
    def __init__(self):
        self.__color = 'red'

    def running(self):
        print('Color: ', self.__color)
        while True:
            if self.__color == 'green':
                time.sleep(6)
                self.__color = 'red'
                print('Color: ', self.__color)
            elif self.__color == 'red':
                time.sleep(7)
                self.__color = 'yellow'
                print('Color: ', self.__color)
            else:
                time.sleep(2)
                self.__color = 'green'
                print('Color: ', self.__color)



trlight = TrafficLight()
trlight.running()



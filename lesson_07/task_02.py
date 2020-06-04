# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное
#    название.
#    К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
#    Это могут быть обычные числа: V и H, соответственно.
#    Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
#    Проверить работу этих методов на реальных данных.
#    Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
#    проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod, abstractproperty


# Этот вариант с использованием дескриптора. Честно взял из интернета как работает почти понял, но не по методичке.  Но эффект интересный с листом в конце


class Clothes(ABC):

    @abstractmethod
    def _calculate(self, x):
        pass


class Coat(Clothes):
    """Пальто, параметр v - размер """
    __consumption = 0

    def __init__(self, v: float):
        self.v = v
        Coat.__consumption += self._calculate()

    def _calculate(self):
        return self.v/6.5 + 0.5

    @property
    def consumption(self):
        return round(Coat.__consumption, 2)

    def __del__(self):
        Coat.__consumption -= self._calculate()


class Suit(Clothes):
    """Костюм, параметр h - рост """
    __consumption = 0

    def __init__(self, h: float):
        self.h = h
        Suit.__consumption += self._calculate()

    def _calculate(self):
        return 2 * self.h + 0.3

    @property
    def consumption(self):
        return round(Suit.__consumption, 2)

    def __del__(self):
        Suit.__consumption -= self._calculate()


s1 = Suit(2)
print ('Требуется ткани для Костюмов: ', s1.consumption)
s2 = Suit(1.8)
print ('Требуется ткани для Костюмов: ', s1.consumption)
c1 = Coat(48)
print ('Требуется ткани для Пальто: ', c1.consumption)
s3 = Suit(1.8)
print ('Требуется ткани для Костюмов: ', s1.consumption)
del( s3)
print ('Требуется ткани для Костюмов: ', s1.consumption)

print('Всего: ', str(s1.consumption + c1.consumption))

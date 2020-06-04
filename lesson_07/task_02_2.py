# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное
#    название.
#    К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
#    Это могут быть обычные числа: V и H, соответственно.
#    Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
#    Проверить работу этих методов на реальных данных.
#    Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
#    проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod, abstractproperty


# Очень хотелось property на атрибут класса.
#  Этот вариант с использованием дескриптора. Честно взял из интернета, как работает почти понял, но не по методичке. 
#  эффект интересный с листом в конце

class classproperty():

    def __init__(self, fget):
        self.fget = fget

    def __get__(self, owner, cls):
        return self.fget(cls)


class Clothes(ABC):
    __consumption = 0

    def __init__(self, x: float):
        self.x = x
        Clothes.__consumption += self._calculate()

    @abstractmethod
    def _calculate(self):
        pass

    @classproperty
    def consumption(self):
        return 'Всего ткани требуется: ' + str(round(Clothes.__consumption,2))

    def __del__(self):
        Clothes.__consumption -= self._calculate()


class Coat(Clothes):
    """Пальто, параметр x - размер """

    def _calculate(self):
        return self.x/6.5 + 0.5


class Suit(Clothes):
    """Костюм, параметр x - рост """

    def _calculate(self):
        return 2 * self.x + 0.3


cl = []
print(Clothes.consumption)
cl.append(Suit(2))
print(Clothes.consumption)
cl.append(Coat(48))
print(Clothes.consumption)
cl.append(Suit(1.8))
print(Clothes.consumption)
cl.pop()
print(Clothes.consumption)

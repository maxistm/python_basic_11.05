# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

# С заданием возможно перемудрил

import uuid

class MyError(Exception):
    pass

class OfficeEquipment:
    def __init__(self, name, width, height, weight):
        self.id = uuid.uuid4()
        self.name = name
        self.width = width
        self.height = height
        self.weight = weight


class OfficeEquipmentSkladPos:
    """
    Класс генерирующий инвентарный номер uuid  на каждую позицию, и хранящий местоположение вещи на складе
    """
    def __init__(self, officeEq: OfficeEquipment):
        self.officeEq = officeEq
        self.idPos = uuid.uuid4()
        self.position = -1     # место на складе (координаты)

    def __str__(self):
        return self.idPos


class SkladOffice:
    """
    Класс склад с типом FIFO первый вошел первый вышел
    """
    def __init__(self, name, adress):
        self.__id = uuid.uuid4()
        self.name = name
        self.adress = adress
        self.maxpos = 5000  # количество мест на складе
        self.__officeEqs = {}
        self.__positions = set()  # позиции на складе (координаты, номера ячеек)
        self.__countNom = {} # количество по Номенклатуре (промежуточные остатки)

    def getFreePosition(self, officeEquipmentSkladPos: OfficeEquipmentSkladPos):
        """
        Поиск свободной ячейки на складе
        """
        i = 0
        while i < self.maxpos:
            if not i in self.__positions:
                officeEquipmentSkladPos.position = i
                self.__positions.add(i)
                return i
            i += 1
        print('Больше нет места')
        officeEquipmentSkladPos.position = -1
        return -1
    
    
    def getCountNom(self, officeEq : OfficeEquipment):
        if officeEq in self.__countNom:
            return self.__countNom[officeEq]
        else:
            return 0

    def getofficeEquipmentSkladInv(self, officeEq: OfficeEquipment):
        """
        Возвращает номеклатуру по складской позиции
        """
        for eq in self.__officeEqs:
            if eq.officeEq == officeEq:
                return eq
        return None

    def getofficeEqusStr(self):
        """
        Вывести все позиции склада
        """
        tmp = '\nСклад '+ self.name + '\n'
        var_str = ''
        for key, eq in self.__officeEqs.items():
            var_str += eq.officeEq.name + '  ' + \
                str(eq.idPos) + '  позиция: ' + \
                str(eq.position) + '\r\n'
        if var_str == '':
            return tmp + 'Пустой'
        return tmp + var_str

    def addItemInv(self, officeEquipmentSkladInv: OfficeEquipmentSkladPos):
        """
        Добавление позиции на склад Инвентарная единица имеющая uuid
        """
        # Добавление или обновление
        if not officeEquipmentSkladInv in self.__officeEqs:
            # получение свободной ячеки (координаты)
            self.getFreePosition(officeEquipmentSkladInv)
            if not officeEquipmentSkladInv.officeEq in self.__countNom:
                # инициализация типа на складе (если не было)
                self.__countNom[officeEquipmentSkladInv.officeEq] = 0
            # прибавление количества + 1 если это добавление
            self.__countNom[officeEquipmentSkladInv.officeEq] += 1

        self.__officeEqs[officeEquipmentSkladInv] = officeEquipmentSkladInv

        return officeEquipmentSkladInv.position

    def addItem(self, officeEq: OfficeEquipment):
        """
        Добавление позиции на склад по номенклатуре
        """
        officeEquipmentSkladInv = OfficeEquipmentSkladPos(officeEq)
        return self.addItemInv(officeEquipmentSkladInv)

    def delItemInv(self, officeEquipmentSkladInv: OfficeEquipmentSkladPos):
        """
        Удаление позиции со склада Инвентарная единица (uuid)
        """
        # освобождение места
        self.__positions.remove(officeEquipmentSkladInv.position)
        # уменьшение количества
        self.__countNom[officeEquipmentSkladInv.officeEq] -= 1
        del self.__officeEqs[officeEquipmentSkladInv]

    def delItem(self, officeEq: OfficeEquipment):
        """
        Удаление позиции со склада по Номенклатуре
        """
        officeEquipmentSkladInv = self.getofficeEquipmentSkladInv(officeEq)
        self.delItemInv(officeEquipmentSkladInv)

    def prihod(self, officeEq: OfficeEquipment, count):
        """
        Приход на склад по Номенклатуре, с раздачей uuid и позиции на складе
        """
        i = 0
        while i < count:
            self.addItem(officeEq)
            i += 1

    def rashod(self, officeEq: OfficeEquipment, count):
        try:
            if count > self.__countNom[officeEq]:
                raise MyError('На складе: ' + self.name + ' столько нет. Остаток: ' + str(self.__countNom[officeEq]))
            i = 0
            while i < count:
                self.delItem(officeEq)
                i += 1
        except Exception as e:
            print('Ощибка: ', e)

    def peremeshenie(self, skladKuda, officeEq, count):
        """
        Перемещение между складами с сохранением uuid
        """
        try: 
            count = int(count)
            if type(skladKuda) != type(self):
                raise MyError('Объект куда перемещение не является складом')
            if count > self.__countNom[officeEq]:
                raise MyError('На складе: ' + self.name + ' столько нет. Остаток: ' + str(self.__countNom[officeEq]))
            i = 0
            while i < count:
                officeEquipmentSkladInv = self.getofficeEquipmentSkladInv(officeEq)
                self.delItemInv(officeEquipmentSkladInv)
                skladKuda.addItemInv(officeEquipmentSkladInv)
                i += 1
        except Exception as e:
            print('Ошибка:', e)


class Printer(OfficeEquipment):

    def __init__(self, name, width, height, weight, color, formatp):
        self.color = color
        self.formatp = formatp
        super().__init__(name, width, height, weight)


class Scaner(OfficeEquipment):
    def __init__(self, name, width, height, weight, resolution, formatp):
        self.resolution = resolution
        self.formatp = formatp
        super().__init__(name, width, height, weight)


class Xerox(OfficeEquipment):
    def __init__(self, name, width, height, weight, color, resolution, formatp):
        self.color = color
        self.resolution = resolution
        self.formatp = formatp
        super().__init__(name, width, height, weight)


# Создаем склады
sclad1 = SkladOffice('СкЛенина1', 'Ленина 1')
podrazdelenie1 = SkladOffice('ПодраздПушкина10', 'Пушкина 10')


# Номенклатура
pr1 = Printer('cannon 1010', 40, 30, 2, 'monohrom', 'A4')
xr1 = Xerox('HP 2031', 50, 60, 12, 'color', '1080p', 'A3')

# Добавление единыцы
sclad1.addItem(xr1)
# Добавление 5 шт.
sclad1.prihod(pr1, 5)


print('Количество: ' + pr1.name + ' на складе: ' + sclad1.name + '  ' + str(sclad1.getCountNom(pr1)))
print(sclad1.getofficeEqusStr())

# Удажение единыцы
sclad1.delItem(pr1)
sclad1.rashod(pr1, 2)

print('Количество: ' + pr1.name + ' на складе: ' + sclad1.name + '  ' + str(sclad1.getCountNom(pr1)))
print('Количество: ' + pr1.name + ' на складе: ' + podrazdelenie1.name + '  ' + str(podrazdelenie1.getCountNom(pr1)))
print(sclad1.getofficeEqusStr())
print(podrazdelenie1.getofficeEqusStr())

sclad1.peremeshenie(podrazdelenie1, pr1, 2)
print(sclad1.getofficeEqusStr())
print(podrazdelenie1.getofficeEqusStr())
print('Количество: ' + pr1.name + ' на складе: ' + sclad1.name + '  ' + str(sclad1.getCountNom(pr1)))
print('Количество: ' + pr1.name + ' на складе: ' + podrazdelenie1.name + '  ' + str(podrazdelenie1.getCountNom(pr1)))

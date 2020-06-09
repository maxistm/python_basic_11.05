# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. 
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class OfficeEquipment:
    def __init__(self, guid, name, width, height, weight):
        self.guid = guid
        self.name = name
        self.width = width
        self.height = height
        self.weight = weight
        self.position = 0


class Sklad:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.maxpos = 500 # количество мест на складе
        self.officeEqs = {}
        self.positions = set()
    
    def getFreePosition(self):
        i = 0
        while i < self.maxpos:
            if not i in self.positions:
                return i
            i += 1
        print('Больше нет места')
        return -1
            

    def addUpdateItem(self, officeEq: OfficeEquipment):
        officeEq.position = self.getFreePosition()
        self.officeEqs[officeEq.guid] = officeEq

    def delItem(self, officeEq: OfficeEquipment):
        self.positions.remove(officeEq.position)
        officeEq.position = 0
        del self.officeEqs[officeEq.guid] 



class Printer(OfficeEquipment):
    
    def __init__(self, guid, name, width, height, weight, color, formatp):
        self.color = color
        self.formatp = formatp
        super().__init__(guid, name, width, height, weight)

class Scaner(OfficeEquipment):
    def __init__(self, guid, name, width, height, weight, resolution, formatp):
        self.resolution = resolution
        self.formatp = formatp
        super().__init__(guid, name, width, height, weight)

class Xerox(OfficeEquipment):
    def __init__(self, guid, name, width, height, weight, color, resolution, formatp):
        self.color = color
        self.resolution = resolution
        self.formatp = formatp
        super().__init__(guid, name, width, height, weight)

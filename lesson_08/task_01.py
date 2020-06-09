# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. 
#    Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен 
#    проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    __datestring = ''
    def __init__(self, datestring):
        Date.__datestring = datestring

    @classmethod
    def getElement(cls, typeofdate):
        temp = cls.__datestring.split('-')
        if len(temp)==3:
            if typeofdate == 'y':
                return int(temp[2])
            if typeofdate == 'm':
                return int(temp[1])
            if typeofdate == 'd':
                return int(temp[0])
        return None


    @staticmethod
    def validation(cls:Date):        
        year = cls.getElement('y')
        mounth = cls.getElement('m')
        day = cls.getElement('d')
        num_days=[31,28,31,30,31,30,31,31,30,31,30,31]
        
        if not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
             num_days[1] = 29
      
        if year < 0:
            return 'Год не может быть отрицательным, или это до н.э.'
        if mounth > 12:
            return 'Месяц не может быть больше 12.'
        if day > num_days[mounth-1]:
            return 'Дней в меяце ' + str(mounth)  + ' не может быть > ' + str(num_days[mounth-1])


dt1 = Date('10-12-84')
print(Date.getElement('d'), Date.getElement('m'), Date.getElement('y'))
dt2 = Date('32-02-2020')
print('Атрибут класса поменялся: ', Date.getElement('d'), Date.getElement('m'), Date.getElement('y'))

print(Date.validation(Date))
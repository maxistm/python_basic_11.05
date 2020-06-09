# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
#   Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
#   Проверьте корректность полученного результата.

import cmath

#x = complex(1,3)



class ComplexInt:

    def __init__(self, a, b:float = None):
        if b != None:
            self.a = a
            self.b = b
        else:
            a = a.replace('i','').replace('j','')
            tmp = a.split('+')
            if len(tmp)==2:
                self.a = float(tmp[0])
                self.b = float(tmp[1])
            else:
                tmp = a.split('-')
                if len(tmp)>2:
                    self.a = -float(tmp[1])
                    self.b = -float(tmp[2])
                else:
                    self.a = float(tmp[0])
                    self.b = -float(tmp[1])

    def __add__(self, other):
        if type(other) != type(self):
            print('Переменная не комплексная')
            return None
        new_a = self.a + other.a
        new_b = self.b + other.b
        return ComplexInt(new_a, new_b)
    
    def __mul__(self, other):
        new_a = self.a * other.a + self.b * other.b * (-1)
        new_b = self.b * other.a + self.a * other.b
        return ComplexInt(new_a, new_b)

    
    def __str__(self):
        var = '{0:g}'.format(self.a)
        if self.b > 0:
            var += '+' + '{0:g}'.format(self.b) +'i'
        else:
            var += '{0:g}'.format(self.b)+'i'
        return var

x = ComplexInt('1.5-3i')
y = ComplexInt(2,-5)
z = x * y
print(z)


x = complex(1.5,-3)
y = complex(2,-5)
z = x * y
print(z)


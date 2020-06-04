# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования 
#    матрицы. 
#    Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#    Примеры матриц вы найдете в методичке.
#    Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#    Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#    Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
import random

class Matrix:
    def __init__(self, matrx):
        demALen = len(matrx[0])
        for line in matrx:
            if len(line) != demALen:
                    raise Exception("Объект не матрица, а разношерсный список:")
            for x in line:            
                x = int(x)
        self.matrx = matrx

    def __str__(self):
        matrixStr = ''
        for line in self.matrx:
            matrixStr += str(line) + '\n'
        return matrixStr

    def __add__(self, other):
        m = []
        if len(self.matrx) != len(other.matrx)  or len(self.matrx[0]) != len(other.matrx[0]):
            return "Матрицы разных порядков"
        i = 0
        while i<len(self.matrx):
            m.append(list(map(sum, zip(self.matrx[i], other.matrx[i]))))
            i += 1
        return Matrix(m)
        
        

def genMatrix(demA, demB, maxInt):
    m = []
    y = 0 
    while y < demB:
        m.append( random.choices(range(maxInt), k=demA) )
        y += 1
    return m

m1 = Matrix(genMatrix(3,3,10))
print(m1)
m2 = Matrix(genMatrix(3,3,10))
print(m2)


print (m1 + m2)


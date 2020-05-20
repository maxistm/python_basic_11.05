# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

my_func = lambda x, y: x ** y


def my_func2(x, y):
    i, tmp = -1, x
    #if y == 0 : return 1
    while i > y:
        tmp *= x
        i -= 1
    return 1 / tmp


while True:
    try:
        x = input('Введите действительное положительное число: ')
        x = float(x)
        if x > 0:
            break
        else:
            print('Число не положительное')
    except Exception as e:
        print('Вы ввели не число', e)

while True:
    try:
        y = input('Введите целое отрицательное число: ')
        y = int(y)
        if y < 0:
            break
        else:
            print('Число не отрицательное')
    except Exception as e:
        print('Число не целое ', e)

print('Ответ x^(y) **:',  my_func(x, y))
print('Ответ x^(y) цикл:',  my_func2(x, y))

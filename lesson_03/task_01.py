# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_div(a, b):
    try:
        return a / b
    except (ZeroDivisionError):
        return 0


while True:
    try:
        a, b = input('Введите два числа через ";": ').split(';')
        a = float(a)
        b = float(b)
        break
    except Exception as e:
        print('Вы ввели не число или не через ";":', e)


print('Результат: ', my_div(a, b))

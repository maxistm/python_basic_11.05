# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    return my_list[-1] + my_list[-2]


while True:
    try:
        a, b, c = input('Введите 3 числа через ";": ').split(';')
        a = float(a)
        b = float(b)
        c = float(c)
        break
    except Exception as e:
        print('Вы ввели не число или не через ";" или их не 3:', e)

print('Сумма двух наибольших чисел:', my_func(a, b, c))

#   2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем. 
#   При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    try:
        a,b = input('Введите два числа через пробел: ').split()
        a = float(a)
        b = float(b)
        if b == 0:
            raise MyError("Нельзя делить на 0")
        print('Ответ: ', a/b)
        break

    except ValueError:
        print('Вы ввели не число или не через пробел')

    except MyError as e:
        print(e)

    except Exception as e:
        print(e)
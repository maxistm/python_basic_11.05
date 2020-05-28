# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
#    Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import os
import random
script_dir = os.path.dirname(os.path.abspath(__file__))

try:
    numbers = open(os.path.join(script_dir ,"files/5_numbers.txt"), 'w', encoding='utf8')
    var_list = random.sample(range(1,100), 10)
    numbers.write(' '.join(map(str, var_list)))
    numbers.close()

    aftemod = open(os.path.join(script_dir ,"files/5_numbers.txt"), 'r', encoding='utf8')
    line = aftemod.read()
    aftemod.close()
except Exception as e:
    print('Ошибка: ', e)
    numbers.close()
    aftemod.close()

print('Числа: ', line, '\nСумма: ', sum(map(int,line.split())))
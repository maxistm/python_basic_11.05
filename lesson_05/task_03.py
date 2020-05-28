# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
#    Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
my_f = open(os.path.join(script_dir ,"files/3_sotrudnik.txt"), 'r', encoding='utf8')

employees = {}
sum_oklad = 0
try:
    for line in my_f:
        fam, value = line.split()
        value = float(value)
        if value < (20000):
            print(fam + ' получает менее 20000, его ЗП: ' + str(value))
        employees[fam] = value
        sum_oklad += value
except Exception as e:
    print('Ошибка ввода/вывода: ', e)

my_f.close()
print('Средний оклад: {:0.2f}'.format(sum_oklad/len(employees)) )
# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
my_f = open(os.path.join(script_dir ,"files/1_out_file.txt"), 'r',encoding='utf8')

coun = {}
stroka = 1
for line in my_f:
    coun[str(stroka)] = str(len(line.split()))
    stroka += 1
my_f.close()


for key, value in coun.items():
    print('В строке ' + key + '  ' + value + ' слов')

print('Всего ' + str(stroka-1) + '  строк')

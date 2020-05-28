# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
out_f = open(os.path.join(script_dir ,"files/1_out_file.txt"), 'a')
while True:
    line = input('Введите что-нибудь: ')
    if line == '':
        break
    out_f.write(line+'\n')
out_f.close()
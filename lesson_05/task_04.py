# 4. Создать (не программно) текстовый файл со следующим содержимым:
#    One — 1
#    Two — 2
#    Three — 3
#    Four — 4
#    Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
#    При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

import os

def translate(line, dict_words):
    newline = line
    for key, rus in dict_words.items():
        if key in line:
            newline = newline.replace(key, rus)
            break
    return newline



dict_words = {}
dict_words['One'] = 'Один'
dict_words['Two'] = 'Два'
dict_words['Three'] = 'Три'
dict_words['Four'] = 'Четыре'

script_dir = os.path.dirname(os.path.abspath(__file__))
original = open(os.path.join(script_dir ,"files/4_number.txt"), 'r', encoding='utf8')
aftemod = open(os.path.join(script_dir ,"files/4_number_mod.txt"), 'w', encoding='utf8')

try:
    for line in original:
        aftemod.write(translate(line, dict_words))
except Exception as e:
    print('Ошибка ввода/вывода: ', e)
aftemod.close()
original.close()




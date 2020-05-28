# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
#    практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
#    Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#    Примеры строк файла:
#    Информатика: 100(л) 50(пр) 20(лаб).
#    Физика: 30(л) — 10(лаб)
#    Физкультура: — 30(пр) —

#    Пример словаря:
#    {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import os

def dic_add(subject, str_num, subjects_dict):
    if len(str_num) > 0:
        if not subject in subjects_dict:
            subjects_dict[subject] = 0
        subjects_dict[subject] += int(str_num)
        

subjects_dict = {}

script_dir = os.path.dirname(os.path.abspath(__file__))
with (open(os.path.join(script_dir ,"files/6_subject.txt"), 'r', encoding='utf8')) as file_sub:
    for line in file_sub:
        subject, hours_line = line.split(':')
        str_num = ''
        for item in hours_line:   
            if item.isdigit():
                str_num += item
            else:
                dic_add(subject, str_num, subjects_dict)
                str_num = ''
        dic_add(subject, str_num, subjects_dict)
        
print(subjects_dict)
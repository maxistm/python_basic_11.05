# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
#    Пример строки файла: firm_1 ООО 10000 5000.
#    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
#    Если фирма получила убытки, в расчет средней прибыли ее не включать.
#    Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
#    Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#    Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#    Итоговый список сохранить в виде json-объекта в соответствующий файл.
#    Пример json-объекта
#    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

#    Подсказка: использовать менеджеры контекста.
import os
import json


script_dir = os.path.dirname(os.path.abspath(__file__))
dict_firms = {}
all_profit = 0
count_profit = 0
with (open(os.path.join(script_dir ,"files/7_firms.txt"), 'r', encoding='utf8')) as file_firm:
    for line in file_firm:
        name, form, income, costs = line.split()
        profit = float(income) - float(costs)
        dict_firms[name] = profit
        if profit >= 0:
            all_profit += profit
            count_profit += 1

average = round(all_profit / count_profit, 2)
dict_pr = {'average_profit': average}
var_list = [dict_firms, dict_pr]

with open(os.path.join(script_dir ,"files/7_itog.json"), "w") as write_f:
    json.dump(var_list, write_f)
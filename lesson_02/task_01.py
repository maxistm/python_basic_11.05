#1. Создать список и заполнить его элементами различных типов данных

var_list = ['Текст', 3, 4.5, None, False, [3,5], {'key': 'value', 'key2': 'value2'}, {'key','ke2'}, ('4',5)]
count = 0
for item in var_list:
    if str == type(item):
        print("Номер списка", count, "- строка: ", type(item))
    elif float == type(item):
        print("Номер списка", count, "- число с запятой: ", type(item))
    elif int == type(item):
        print("Номер списка", count, "- число: ", type(item))
    elif type(None) == type(item):
        print("Номер списка", count, "- пустой тип: ", type(item))
    elif bool == type(item):
        print("Номер списка", count, "- булеан: ", type(item))
    elif list == type(item):
        print("Номер списка", count, "- список: ", type(item))
    elif dict == type(item):
        print("Номер списка", count, "- словарь: ", type(item))
    elif set == type(item):
        print("Номер списка", count, "- сет: ", type(item))
    elif tuple == type(item):
        print("Номер списка", count, "- тапл: ", type(item))
    count += 1
    
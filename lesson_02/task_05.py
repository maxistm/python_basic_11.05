# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.

my_list = [7, 5, 3, 3, 2]
print('Начальный список:', my_list)
while True:
    var_num = input('Введите число  ("q" - выход): ')
    if var_num == 'q':
        break
    if var_num.isdigit():
        var_num = int(var_num)
        start = 0
        end = len(my_list) 
        while start != end:
            search = (end - start) // 2 + start
            if var_num <= my_list[search]:
                start = search + 1
            else:
                end = search
        my_list.insert(end, var_num)
        print(my_list)
    else:
        print('Вы вели не число')

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
while True:
    var_num = input('Введите месяц в виде целого числа от 1 до 12: ')
    if var_num.isdigit():
        var_num = int(var_num)
        if (1 <= var_num <= 12):
            break
        else:
            print('Вы ввели число не в том диапазоне.')
    else:
        print('Вы вели не число')
if var_num == 12:
    var_num = 0    
var_list = ['Зима','Весна','Лето','Осень']
var_dict = {0:'Зима',1:'Весна',2:'Лето',3:'Осень'}
period = (var_num-1) // 3
print('Время года по списку: ', var_list[period])
print('Время года по словарю то же: ', var_dict[period])

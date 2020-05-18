# 2. Для списка реализовать обмен значений соседних элементов

var_list = input('Введите элементы списка через ",":  ').split(',')

print('Первоначальный список: ', var_list)
i = 1
while i < len(var_list):
    tmp = var_list[i]
    var_list[i] = var_list[i-1]
    var_list[i-1] = tmp
    i += 2
print('Полученный список: ', var_list)

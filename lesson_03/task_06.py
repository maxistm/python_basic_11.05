# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
#    Например, print(int_func(‘text’)) -> Text.
#    Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
#    Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
#    Необходимо использовать написанную ранее функцию int_func().

def int_func(var_string): return var_string[0].upper() + var_string[1:]


while True:
    var_string = input(
        'Введите предложение из прописных латинских букв через пробел: ')
    no_lat = 0
    for symbol in var_string:
        var_ascii = ord(symbol)
        if 67 <= var_ascii <= 122 or var_ascii == 32:
            continue
        else:
            print('Слово содержит не прписной латинский символ')
            no_lat = 1
            break
    if no_lat == 0:
        break


words = var_string.split()
print('Новая строка: ')
for word in words:
    print(int_func(word), end=' ')

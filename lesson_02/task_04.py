# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.

var_str = input('Введите строку из нескольких слов через пробел: ').split(' ')
i = 0
for word in var_str:
    if (len(word)>10):
        print(str(i) +': ' + word[0:10])
    else:
        print(str(i) +': ' + word)
    i += 1

# Можно было и просто, чтоб лишний раз не копировался массив 
# i = 0
# for word in var_str:
#     if (len(word)>10):
#         print(str(i) +': ' + word[0:10])
#     i += 1
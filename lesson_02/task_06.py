# 6. * Реализовать структуру данных «Товары».

name = 'название'
price = 'цена'
count = 'количество'
ed = 'ед'

#goods = [
#(1, {name: 'компьютер', price: 20000, count: 5, ed: 'шт.'}),
#(2, {name: 'принтер', price: 6000, count: 2, ed: 'шт.'}), 
#(3, {name: 'сканер', price: 2000, count: 7, ed: 'шт.'})
#]
goods = []

print('Введите товар с характеристиками')

yesno = 'y'
while yesno != 'n':
    item = {}
    item[name] = input('Введите наименование: ')
    while True: 
        var_price = input('Введите цену: ')
        if var_price.isdecimal():
            item[price] = int(var_price)
            break
        else:
            print("Вы ввели не число")
    while True: 
        var_price = input('Введите количество: ')
        if var_price.isdigit():
            item[count] = int(var_price)
            break
        else:
            print("Вы ввели не число")
    item[ed] = input('Введите ед. изм.: ')
    goods.append((len(goods),item))
    yesno = input('Ввести еще товар? ("n" - отказ)')

table = {}
for good in goods:
    for key,value in good[1].items():
        if not key in table:
            table[key] = [value]
        else:
            table[key].append(value)

print(table)
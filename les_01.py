print('#1. ввод/вывод')
print('#2. часы')
print('#3. cумма n')
print('#4. Найдите самую большую цифру в числе')
print('#5. Запросите у пользователя значения выручки')
print('#6. Спортсман')
zadacha = input('Выберите задачу  (0 - все): ')
if zadacha.isdigit() == False:
    exit() 
zadacha = int(zadacha)

#1. ввод/вывод
if zadacha == 0 or zadacha == 1:
    print('Задача #1. ввод/вывод')
    number = input('Введите число: ')
    if number.isdigit():
        print('Число: ',  number)
    else:
        print('Вы ввели не число: ',number)

    string = input('Введите текст: ')
    print('Текст: ', string)

#2. часы
if zadacha == 0 or zadacha == 2:
    print('Задача #2. часы')
    secinput = input('Введите количество секунд: ')
    if secinput.isdigit():
        secinput = int(secinput)
        hour = secinput // 3600
        minuts = (secinput - hour * 3600) // 60
        sec = secinput - hour * 3600 - minuts * 60
        print('{:02}'.format(hour)  , '{:02}'.format(minuts), '{:02}'.format(sec), sep=':')
    else:
        print('Вы ввели не число или оно отрицательное: ',secinput)

#3. cумма n
if zadacha == 0 or zadacha == 3:
    print('Задача #3. cумма n')
    n = input('Введите число чтобы получить сумму  n + nn + nnn: ')
    if n.isdigit():
        nn = n + n
        nnn = nn + n
        sum = int(n) + int(nn) + int(nnn)
        print('Сумма ',n,'+',nn,'+',nnn,'=',   sum  )
    else:
        print('Вы ввели не число или оно отрицательное: ',n)

#4. Найдите самую большую цифру в числе
if zadacha == 0 or zadacha == 4:
    print('Задача #4. Найдите самую большую цифру в числе')
    number = input('Введите число: ')
    if number.isdigit():
        maxt=0
        for digit in number:
            if int(digit) > maxt:
                maxt = int(digit)
        print('Максимальная цифра: ', maxt)
    else:
        print('Вы ввели не число или оно отрицательное: ',number)

#5. Запросите у пользователя значения выручки 
if zadacha == 0 or zadacha == 5:
    print('Задача #5. Запросите у пользователя значения выручки')
    revenue = input('Введите выручку: ')
    costs = input('Введите издержки: ')
    try:
        revenue = float(revenue)
        costs = float(costs)
        result = revenue - costs
        if result > 0:
            print('Ваша фирма работает с прибылью ', result)
            ren = round(result / revenue * 100,2)
            print('Рентабельность: '+ str(ren)+'%')
            employee = input('Введите кол-во сотрудников: ')
            if employee.isdigit():
                print('Прибыль на одного сотрудника: ' + str(round(result/int(employee),2)) )
            else:
                print('Сотрудники должны измеряться в цифрах: ', employee)
        else:
            print('У вас все плохо: ', result )
    except (TypeError, ValueError):
        print('Вы ввели не число в одно или оба значения: ',revenue, costs)
    
#6. Спортсман
if zadacha == 0 or zadacha == 6:
    print('Задача #6. Спортсман')
    start = input('Введите стартовый километраж "a": ')
    target = input('Введите цель "b": ')
    try:
        start = float(start)
        target = float(target)
        day  = 1
        while start < target:
            print(str(day) + '-й день: ' + str(round(start,2) ) )
            start = start * 1.1
            day += 1
        print(str(day)+'-й день: ' + str(round(start,2) ) )
        print('На '+str(day)+'-й день спортсмен достиг результата — не менее',target,'км.')
    except (TypeError, ValueError):
        print('Вы ввели не число в одно или оба значения: ',start, target)
# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
#    Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def input_custumer(name, surname, birth_year, city, email, phone):
    print('Имя:', name, '  Фамилия:', surname, '  Год рождения:', birth_year, 
          '  Город проживания:', city, '  email:', email, '  Телефон:', phone)


name = 'Ivan'
surname = 'Ivanov'
year = 1980
city = 'Ivanovsk'
mail = 'ivanovi@mail.ru'
phone = 79123456789

input_custumer(surname=surname, name=name, birth_year=year,
               city=city, phone=phone, email=mail)



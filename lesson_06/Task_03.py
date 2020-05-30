#   3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). 
#    Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
#    Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и 
#    дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить 
#    значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage":wage, "bonus":bonus}

class Position(Worker):
    
    def get_full_name(self) -> str:
        return self.name + ' ' + self.surname

    def get_total_income(self) -> float:
        return self._income["wage"] + self._income["bonus"]

workers = []
workers.append(Position('Василий', 'Иванов', 'Сварщик', 40000, 20000))
workers.append(Position('Петр', 'Петров', 'Токарь', 30000, 15000))

for w in workers:
    print(w.get_full_name(), " доход: ", w.get_total_income())



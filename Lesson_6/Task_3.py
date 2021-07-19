# Выполнено
# 3.Реализовать базовый класс Worker (работник).#
# ●	определить атрибуты: name, surname, position (должность), income (доход);
# ●	последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
#                    оклад и премия, например, {"wage": wage, "bonus": bonus};
# ●	создать класс Position (должность) на базе класса Worker;
# ●	в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учётом премии (get_total_income);
# ●	проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.
class Worker:
    # атрибут класса
    count = 0
    # методы класса


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        Worker.count += 1
        print(Worker.count, name, surname, position, wage, bonus)

    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return full_name

    def get_total_income(self):
        total_income = sum(self._income.values())
        return total_income


worker_1 = Position("Мария", "Андреева", "Консультант", 1000, 500)
worker_2 = Position("Ольга", "Варгасова", "Стажер", 700, 400)
print()
# Проверка атрибутов и методов
print(worker_1.get_full_name(), worker_1.get_total_income())
print(worker_2.get_full_name(), worker_2.get_total_income())
print("Общее количество сотрудников:", Worker.count)

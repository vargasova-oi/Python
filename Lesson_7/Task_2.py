# Выполнено
# 2.Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    # атрибуты класса
    count = 0
    outlay = 0

    # конструктор - атрибуты объекта
    def __init__(self, name, size):
        self.name = name
        self.size = size
        Clothes.count += 1
        print(Clothes.count, name, size)

    # обязательный базовый метод для всех потомков
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):

    def fabric_consumption(self):
        Clothes.outlay += round(self.size / 6.5 + 0.5, 1)
        return round(self.size / 6.5 + 0.5, 1)

    @property
    def my_print(self):
        return f"Расход ткани на {self.name} составит {self.fabric_consumption()} м."


class Suit(Clothes):

    def fabric_consumption(self):
        Clothes.outlay += round(self.size * 2 + 0.3, 1)
        return round(self.size * 2 + 0.3, 1)

    @property
    def my_print(self):
        return f"Расход ткани на {self.name} составит {self.fabric_consumption()} м."


coat_1 = Coat("Пальто осеннее", 46)
suit_1 = Suit("Деловой костюм", 1.7)
coat_2 = Coat("Пальто весеннее", 48)
# Проверка атрибутов и методов
print()
print(coat_1.my_print)
print(suit_1.my_print)
print(coat_2.my_print)
print()
print(f"Общий расход ткани: {round(Clothes.outlay, 1)} м.")

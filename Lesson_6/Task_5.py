# Выполнено
# 5.Реализовать класс Stationery (канцелярская принадлежность).
# ●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# ●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ●	в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# ●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    # атрибут класса
    title = "Название канцелярской принадлежности"

    # методы класса

    def draw(self, title):
        self.title = title
        print(f"Запуск отрисовки")


class Pen(Stationery):
    def draw(self, title):
        self.title = title
        print("Запуск:", self.title)


class Pencil(Stationery):
    def draw(self, title):
        self.title = title
        print("Отрисовка:", self.title)


class Handle(Stationery):
    def draw(self, title):
        self.title = title
        print("Запуск отрисовки:", self.title)


a = Pen()
a.draw("красный карандаш")

a = Pencil()
a.draw("зеленая ручка")

a = Handle()
a.draw("черный маркер")

# Выполнено
# 4.Реализуйте базовый класс Car.#
# ●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# ●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# ●	для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
class Car:
    # атрибуты класса
    count = 0
    is_police = False
    # конструктор - атрибуты объекта

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        Car.count += 1
        print(Car.count, speed, color, name)

    # методы класса
    def go(self):
        print(f"Поехала: {self.name}")

    def stop(self):
        print(f"Остановилась: {self.name}")

    def turn(self, turn):
        turn = turn
        print(f"Повернула: {self.name} {turn}")

    def show_speed(self):
        print(f"Скорость: {self.name} {self.speed}")


class TownCar(Car):
    is_police = False

    def show_speed(self):
        print(f"Скорость: {self.name} {self.speed}") if self.speed <= 60 \
            else print(f"Внимание! Превышение скорости: {self.name} {self.speed}")


class WorkCar(Car):
    is_police = False

    def show_speed(self):
        print(f"Скорость: {self.name} {self.speed}") if self.speed <= 40 \
            else print(f"Внимание! Превышение скорости: {self.name} {self.speed}")


class SportCar(Car):
    is_police = False


class PoliceCar(Car):
    is_police = True


town_car_1 = TownCar(70, "бирюзовый", "BMW")
work_car_1 = WorkCar(30, "белый", "Lada")
police_car_1 = PoliceCar(100, "синий", "Opel")
print()
# Проверка атрибутов
print(f"Полицейская ли машина: {town_car_1.name} {town_car_1.is_police}")
print(f"Полицейская ли машина: {police_car_1.name} {police_car_1.is_police}")
# Проверка методов
town_car_1.go()
town_car_1.stop()
town_car_1.turn("left")
town_car_1.show_speed()
work_car_1.show_speed()

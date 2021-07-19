# Выполнено
# 1.Создать класс TrafficLight (светофор).
# ●	определить у него один атрибут color (цвет) и метод running (запуск);
# ●	атрибут реализовать как приватный;
# ●	в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# ●	продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# ●	переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# ●	проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.
import time


def create_countdown_timer(timer):
    print(timer, "......")


class TrafficLight:
    # атрибут класса
    __color = "цвет"

    # методы класса

    def running(self):
        self.__color = "красный"
        print(self.__color)
        local_time = 7
        for times in range(local_time):
            # call the function and pass the current time left
            create_countdown_timer(local_time - times)
            # call the function in every 1 second.
            time.sleep(1)
        self.__color = "желтый"
        print(self.__color)
        local_time = 2
        for times in range(local_time):
            # call the function and pass the current time left
            create_countdown_timer(local_time - times)
            # call the function in every 1 second.
            time.sleep(1)
        self.__color = "зеленый"
        print(self.__color)
        local_time = 5
        for times in range(local_time):
            # call the function and pass the current time left
            create_countdown_timer(local_time - times)
            # call the function in every 1 second.
            time.sleep(1)
        print("Электричество кончилось")


a = TrafficLight()
a.running()

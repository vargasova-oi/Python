# Выполнено
sec = int(input("Укажите время в секундах: "))
hour = sec // 3600
mi = (sec % 3600) // 60
sec = (sec % 3600) % 60
print(f"Сейчас: {hour:02}:{mi:02}:{sec:02}")

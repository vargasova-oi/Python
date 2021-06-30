sec = int(input("Укажите время в секундах: "))
hour = sec // 3600
mi = (sec % 3600) // 60
sec = (sec % 3600) % 60
print(f"Сейчас: {hour:2}:{mi:2}:{sec:2}")

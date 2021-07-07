# 1.Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
def func_salary(x, y, z):
    """Расчитывает зарплату: выработка * ставку + премия"""
    try:
        x, y, z = float(x), float(y), float(z)
        s = (x * y) + z
        # return x, y, z, s
        return f'Выработка = {x}, ставка = {y}, премия = {z}. Зарплата сотрудника: {round(s, 0)}'
    except ValueError:
        return "Программа работает только с числами."

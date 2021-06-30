# Выполнено
n = int(input("Укажите число n: "))
nn = int(str(n) + str(n))
nnn = int(str(n) + str(n) + str(n))
summa = n + nn + nnn
print(f"Сумма n + nn + nnn = {n} + {nn} + {nnn} = {summa}")

# Вариант преподавателя:
# n = input("Укажите число n: ")
# print(f"Сумма {n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")

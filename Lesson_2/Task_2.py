# Выполнено
# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().
p = input("Укажите несколько слов через пробел: ")
# разбивает строку на список, состоящий из слов
my_list = p.split()
# узнаем длину списка
N = len(my_list)
n = 0
# вывод на печать исходных данных
print(f"Список введенных слов: {my_list}")
result_list = []
while n <= N - 2:
    # реверс первых двух элементов
    t_list = my_list[n:n+2][::-1]
    # формируем итоговый спискок из срезов по 2 элемента
    result_list = sum([result_list, t_list], [])
    n += 2
# добавляем хвостик, если нечетное количество строк
if N % 2 != 0:
    result_list = sum([result_list, [my_list[-1]]], [])
# печать ответа
print(f"Ответ после обмена: {result_list}")
# -------------вариант преподавателя-----------
my_list = list(input("Введите цифры без пробелов - "))

for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(my_list)

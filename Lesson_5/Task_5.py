# Выполенено
# 5.Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
from functools import reduce
import random


out_f = open("out_number.txt", "w")
line_list = [random.randint(0, 101) for el in range(0, 10)]
"""Формируется список из десяти чисел от 0 до 100"""
print(line_list)
out_f.writelines(str(line_list)[1:len(str(line_list))-1])
"""В файл записывается список без первого и последнего символа - скобок"""


def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el + el


print(f"Результат суммы чисел: {reduce(my_func, line_list)}")
out_f.close()

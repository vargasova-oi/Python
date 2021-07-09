# Выполнено
# 2.Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.
#
# Строки считаю в файле, который создала в Задании 1
f = open("out_file.txt", "r")
content_list = [str(line) + ' Количество слов: ' + str(len(line.split())) for line in f]
print(content_list, ' Количество строк: ', len(content_list))

# -------------второй способ_____________
# n_str = 0
# for line in f:
#     n_str += 1
#     print(len(line))
#     line_list = line.split()
#     print(len(line_list))
# print(f"Общее количество строк: {n_str}")
# ----------------------------------------

f.close()

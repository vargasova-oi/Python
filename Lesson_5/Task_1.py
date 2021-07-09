# Выполнено
# 1.Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
out_f = open("out_file.txt", "w")
line_list = []
while True:
    line = input("Введите строку текста в файл: ")
    if line == '':
        break
    else:
        line = str(line) + '\n'
        line_list.append(line)
out_f.writelines(line_list)
out_f.close()

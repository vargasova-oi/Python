# Выполнено
# 3.Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
content = open("text_3.txt", "r", encoding='utf-8')
content_list = sum([line.split() for line in content], [])
employee = [content_list[n] for n in range(0, len(content_list)) if n % 2 == 0 and float(content_list[n + 1]) < 20000]
sum_sal = [float(content_list[n]) for n in range(0, len(content_list)) if n % 2 != 0]
av_salary = sum(sum_sal) / len(sum_sal)
print(content_list)
print(employee)
print(av_salary)
content.close()

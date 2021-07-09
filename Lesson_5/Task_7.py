# Выполнено
# 7.Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта: # [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json
with open("text_7.txt", encoding='utf-8') as f_obj:
    content_list = sum([line.split() for line in f_obj], [])
    profit_dict = {str(content_list[n]): int(content_list[n+2]) - int(content_list[n+3])
                   for n in range(0, len(content_list)) if n % 4 == 0}
    profit_list = [int(content_list[n+2]) - int(content_list[n+3]) for n in range(0, len(content_list))
                   if n % 4 == 0 and int(content_list[n+2]) - int(content_list[n+3]) > 0]
    """Список только прибылей, без убытков"""
    avr_profit = {"average_profit": sum(profit_list) / len(profit_list)}
    data = [profit_dict, avr_profit]
    print(content_list)
    print(profit_dict)
    print(profit_list)
    print(avr_profit)
    print(data)
    with open("text_7.json", "w", encoding='utf-8') as write_j:
        json.dump(data, write_j, ensure_ascii=False)

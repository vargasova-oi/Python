# Выполнено
# 4.Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
from textblob import TextBlob

content = open("text_4.txt", "r", encoding='utf-8')
out_f = open("out_file_4.txt", "w", encoding='utf-8')
for line in content:
    blob = TextBlob(str(line.split()[0]))
    out_f.write(str(" ".join([str(blob.translate(to='ru')), line.split()[1], line.split()[2]])) + '\n')
out_f.close()
content.close()

# Выполнено
# 7.Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().
my_list = (input("Введите несколько слов маленькими латинскими буквами: ")).split()
result_list = []
for w in range(0, len(my_list), 1):

    def int_func():
        user_word = my_list[w]
        i = 0
        while i < len(user_word):
            if 96 < ord(user_word[i]) < 123:
                """фильтр на латинские маленькие буквы"""
                i += 1
            else:
                return ''
        return user_word.title()


    user_word_val = int_func()

    result_list.append(user_word_val)

    print(f"Процесс: обрабатывается слово - {user_word_val}, формируется список - {result_list}")

result_str = ' '.join(result_list)
print(f"Итог: Введенный список - {my_list}, результат - {result_str}")

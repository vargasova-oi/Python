# Выполнено
# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
def int_func():
    user_word = str(input("Введите слово маленькими латинскими буквами: "))
    i = 0
    while i < len(user_word):
        if 96 < ord(user_word[i]) < 123:
            """фильтр на латинские маленькие буквы"""
            i += 1
        else:
            return "Ошибка ввода"
    return user_word.title()


user_word_val = int_func()

print(f"{user_word_val}")

# print(int_func(str('text')))

# Выполнено
# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def first_func():
    name = 'Olga'
    surname = 'Var'
    year = 80
    town = 'Moscow'
    mail = 'ulola@mail.ru'
    phone = 75584
    return name, surname, year, town, mail, phone


my_list = first_func()

for el in my_list:
    print(el, end=', ')

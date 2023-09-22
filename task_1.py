'''
1. Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY Функция возвращает истину, 
если дата может существовать или ложь, если такая дата невозможна. Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
Проверку года на високосность вынести в отдельную защищённую функцию. 
'''

from datetime import datetime


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True

    else:
        return False


def get_date(date_str):
    #date_str = input("Введите дату в формате DD.MM.YYYY: ")

    try:
        date_obj = datetime.strptime(date_str, "%d.%m.%Y")
        year = date_obj.year

        if is_leap_year(year):
            print(f"{year} - високосный год")
        else:
            print(f"{year} - не високосный год")

    except ValueError:
        print("Неверный формат даты. Введите дату в формате DD.MM.YYYY.")


#get_date()

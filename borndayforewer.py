"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

def year_birth(year):
    while year != 1799:
        year = int(input('Введите год рождения А.С.Пушкина: '))

def day_birth(day):
    while day != '06.06':
        day = input('Введите дату рождения А.С.Пушкина (в формате dd.mm): ')
    print('Верно!')

born_year = 0
day_born = ''
year_birth(born_year)
day_birth(day_born)
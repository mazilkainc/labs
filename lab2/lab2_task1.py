from math import fabs
money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
counter = 1
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
money_capital = money_capital - spend + salary

while money_capital >= fabs(salary - spend):
    spend = spend + spend*increase
    money_capital = money_capital - spend + salary
    counter += 1

print("Количество месяцев, которое можно протянуть без долгов:", counter)
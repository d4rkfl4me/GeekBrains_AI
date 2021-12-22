# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
#Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
gr_profit = int(input("Введите значение выручки: "))
exp = int(input("Введите значение издержек: "))
net_prof = ((gr_profit - exp) / gr_profit) * 100

if gr_profit > exp:
    print("Поздравляем с удачным финансовым годом! Так держать!")
    print("Рентабельность выручки составила ", f'{net_prof:.2f}')
    staff = int(input("Введите количество сотрудников, задействованных в продажах: "))
    gr_profit_s = (gr_profit - exp) / staff
    print("Удельная прибыль компании в этом году составила ", f'{gr_profit_s:.0f}')
else:
    print("Что-то пошло не так, надо пересмотреть бухгалтерию")
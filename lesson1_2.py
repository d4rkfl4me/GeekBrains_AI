# пользователь вводит время в секундах. Необходимо перевести его в часы, минуты и секунды и вывести в формате чч:мм:сс
sec = int(input("Введите время в секундах: "))
s = sec % 60
m = (sec // 60) % 60
h = sec // 3600
if m < 10:
    m = '0' + str(m)
else:
    m = str(m)
if s < 10:
    s = "0" + str(s)
else:
    s = str(s)
if h < 10:
    h = "0" + str(h)
else:
    h = str(h)
print(h + ':' + m + ':' + s)
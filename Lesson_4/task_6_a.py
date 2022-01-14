from itertools import count

for el in count(int(input('Введите стартовое число '))):
    print(el)
    if el == 10:
        break
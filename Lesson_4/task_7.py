from itertools import count
from math import factorial


def fact():
    for el in count(1):
        yield factorial(el)


gen = fact()
x = 0
n = int(input("Введите число: "))
for i in gen:
    if x < n:
        print(i)
        x += 1
    else:
        break

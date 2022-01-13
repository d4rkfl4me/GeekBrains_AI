from itertools import cycle

my_list = [True, 'ABC', 123, None]
x = 0
for el in cycle(my_list):
    if x > 10:
        break
    print(el)
    x += 1

def div(*args):
    try:
        arg1 = int(input("Введите делимое: "))
        arg2 = int(input("Введите делитель "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Неверный делитель! На ноль делить нельзя"

    return res


print(f'result  {div()}')

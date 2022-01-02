'''
    name = input('enter name')
    surname = input('enter surname')
    year = int(input('enter year'))
    city = input('enter city')
    email = input('enter email')
    telephone = input('input telephone')
'''


def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Yanchenko', name='Yevgeniy', year='1985', city='Almaty', email='rad_zivert@mail.ru',
              telephone='8-747-870-33-05'))
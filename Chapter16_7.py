from datetime import datetime

today = datetime.today()

# print(datetime.datetime.today().weekday())
birthday = datetime(1995, 2, 20)


def birthday_calculator(birthday):
    '''Receive birthday <datetime> and out put years old,
    time to next birthday'''
    year_old = today.year - birthday.year
    print('You are %s years old now' % year_old)
    nextbirthday = datetime(today.year, birthday.month, birthday.day)
    if today > nextbirthday:
        nextbirthday = datetime(today.year + 1, birthday.month, birthday.day)
    time_to_next_birthday = nextbirthday - today
    print(time_to_next_birthday)
    return nextbirthday


def double_day(birth1, birth2, n):
    '''Calculate double date of two person who have birthday on
    birth1 and birth2<datetime>'''
    assert isinstance(birth1, datetime) and isinstance(birth2,
                                                       datetime), 'Input argument are not datetime instance \n please check!!'
    if birth1 == birth2:
        return 'Their age will always be equal!'
    if birth1 > birth2:
        A = birth1
        B = birth2
    else:
        A = birth2
        B = birth1
    dA = (A - B)
    dx = (n * dA) / (n - 1)
    doubleday = B + dx
    return doubleday


if __name__ == '__main__':
    birthday_calculator(birthday)
    birth1 = datetime(2002, 12, 15)
    birth2 = datetime(2006, 6, 24)
    doubleday = double_day(birth1, birth2, 4)
    print(doubleday)
    print(doubleday - birth1)
    print(doubleday - birth2)

from datetime import datetime
def double_day(b1, b2):
    """Compute the day when one person is twice as old as the other.

    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """
    assert b1 > b2
    delta = b1 - b2
    double_day = b1 + delta
    return double_day
# compute the day one person is twice as old as another
b1 = datetime(2006, 12, 26)
b2 = datetime(2003, 10, 11)
print('Double Day')
print(double_day(b1, b2))
dday=double_day(b1, b2)
print(dday-b1)
print(dday-b2)

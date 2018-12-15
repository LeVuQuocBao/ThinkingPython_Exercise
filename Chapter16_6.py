from Chapter16_1 import Time, time_to_sec, sec_to_time


def mul_time(t1, number):
    ''' Multiply t1 <Time> with number <int>
    output: new Time object <Time>'''
    seconds = time_to_sec(t1)
    seconds = seconds * number
    t_out = sec_to_time(seconds)
    return t_out


def average_pace(t1, d):
    ''' Calculate average pace <Time>
    by multiply t1 <Time> with 1 per
    distance (1/d) <f>'''
    t_out = mul_time(t1, 1 / d)
    return t_out


if __name__ == '__main__':
    t1 = Time(1, 20, 0)
    t_mul = mul_time(t1, 4)
    t_mul.print_time()
    pace = average_pace(t1, 20)
    pace.print_time()

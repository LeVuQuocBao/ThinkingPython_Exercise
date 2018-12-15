class Time(object):
    '''Represent time of day
    attribute: hour, minute, second'''

    def __init__(self, hh, mm, ss):
        self.hour = hh
        self.minute = mm
        self.second = ss

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_sec(self):
        '''Convert timeobj <Time> to second with secout <int>'''
        htosec = self.hour * 3600
        mtosec = self.minute * 60
        secout = htosec + mtosec + self.second
        return secout


def time_to_sec(timeobj):
    '''Convert timeobj <Time> to second with secout <int>'''
    htosec = timeobj.hour * 3600
    mtosec = timeobj.minute * 60
    secout = htosec + mtosec + timeobj.second
    return secout


def sec_to_time(se_in):
    '''Convert second back to time object <Time>'''
    time = Time(0, 0, 0)
    minute, time.second = divmod(se_in, 60)
    time.hour, time.minute = divmod(minute, 60)
    return time


def is_after(t1, t2):
    ''' Check if t1 <Time> follow t2 <Time>
     chronologically : True else False'''
    secondt1 = time_to_sec(t1)
    secondt2 = time_to_sec(t2)
    return secondt1 > secondt2


def increment(t1, second):
    '''add number of second <int> to t1 object <Time>
     as a modifier and doesn't contain any loop'''
    t1.second += second
    plus_minute = t1.second // 60
    remain_second = t1.second % 60
    t1.second = remain_second
    t1.minute += plus_minute
    plus_hour = t1.minute // 60
    remain_minute = t1.minute % 60
    t1.minute = remain_minute
    t1.hour += plus_hour


def increment_pure(t1, second):
    '''Increment_pure version to add
    amount of second to t1 <Time> and
    return a new t_tmp <Time> without
    modifying t1'''
    from copy import deepcopy
    t_tmp = deepcopy(t1)
    print(t_tmp is t1)
    t_tmp.second += second
    plus_minute = t_tmp.second // 60
    remain_second = t_tmp.second % 60
    t_tmp.second = remain_second
    t_tmp.minute += plus_minute
    plus_hour = t_tmp.minute // 60
    remain_minute = t_tmp.minute % 60
    t_tmp.minute = remain_minute
    t_tmp.hour += plus_hour
    return t_tmp


def incrementt_insign(t1, second):
    ''' Using Sexagesimal to calculate increment of time'''
    seconds = time_to_sec(t1) + second
    t1_inc_insign = sec_to_time(seconds)
    return t1_inc_insign


if __name__ == '__main__':
    t1 = Time(0, 59, 30)
    t2 = Time(2, 30, 0)
    print(is_after(t1, t2))
    t1.print_time()
    increment(t1, 300)
    t1.print_time()
    t1_inc = increment_pure(t1, 300)
    t1_inc.print_time()
    t1_inc_insign = incrementt_insign(t1, 300)
    t1_inc_insign.print_time()
    print(t1)
    print(t1.time_to_sec())

import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import datetime
def get_today_date():
        return datetime.date.today()
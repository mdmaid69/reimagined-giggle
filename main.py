import datetime
def get_current_date():
        return datetime.date.today()
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
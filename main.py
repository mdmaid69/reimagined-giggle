import datetime
def get_days_until_next_year():
        next_year = datetime.date.today().year + 1
        next_new_year = datetime.date(next_year, 1, 1)
        return (next_new_year - datetime.date.today()).days
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
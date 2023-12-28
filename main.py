import datetime
def get_today_date():
        return datetime.date.today()
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import datetime
def get_current_date():
        return datetime.date.today()
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
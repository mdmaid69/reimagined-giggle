import datetime
def get_current_datetime():
        return datetime.datetime.now()
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
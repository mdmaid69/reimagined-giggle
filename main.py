import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import datetime
def get_current_datetime():
        return datetime.datetime.now()
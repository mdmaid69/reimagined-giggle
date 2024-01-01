import datetime
def get_current_date():
        return datetime.date.today()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
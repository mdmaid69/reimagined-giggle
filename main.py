import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import datetime
def get_today_date():
        return datetime.date.today()
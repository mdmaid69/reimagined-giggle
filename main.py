import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import datetime
def get_today_date():
        return datetime.date.today()
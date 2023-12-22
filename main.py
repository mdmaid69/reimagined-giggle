import datetime
def get_current_datetime():
        return datetime.datetime.now()
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
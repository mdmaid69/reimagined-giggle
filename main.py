import time
def get_time_since_epoch():
        return time.time()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
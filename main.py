import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import time
def get_current_time():
        return time.ctime()
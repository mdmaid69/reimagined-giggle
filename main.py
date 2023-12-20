import datetime
def get_current_datetime():
        return datetime.datetime.now()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
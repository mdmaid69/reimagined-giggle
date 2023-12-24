import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
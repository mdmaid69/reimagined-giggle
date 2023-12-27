import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
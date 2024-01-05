import time
def get_current_time():
        return time.ctime()
import collections
def count_elements(iterable):
        return collections.Counter(iterable)
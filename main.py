import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import collections
def count_elements(iterable):
        return collections.Counter(iterable)
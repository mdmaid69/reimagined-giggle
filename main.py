import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import time
def get_time_since_epoch():
        return time.time()
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
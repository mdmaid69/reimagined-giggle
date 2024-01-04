import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import datetime
def get_current_datetime():
        return datetime.datetime.now()
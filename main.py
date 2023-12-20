import re
def split_string(pattern, string):
        return re.split(pattern, string)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
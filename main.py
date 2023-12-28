import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import re
def split_string(pattern, string):
        return re.split(pattern, string)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
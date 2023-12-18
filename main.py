import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
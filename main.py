import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
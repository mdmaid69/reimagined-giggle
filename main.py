import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import re
print(re.match("h.*o", "hello world"))
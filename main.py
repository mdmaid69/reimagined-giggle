import re
print(re.match("h.*o", "hello world"))
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
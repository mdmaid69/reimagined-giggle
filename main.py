i = 0
while i < 5:
        print(i)
        i += 1
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
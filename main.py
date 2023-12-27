n = 10
print("Powers of 2:", [2**x for x in range(n)])
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
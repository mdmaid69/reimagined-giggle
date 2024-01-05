n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
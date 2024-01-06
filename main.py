n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
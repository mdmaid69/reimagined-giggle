numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
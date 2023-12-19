import random
print(random.randint(0, 100))
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
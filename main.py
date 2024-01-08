import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import itertools
print(list(itertools.permutations([1, 2, 3])))
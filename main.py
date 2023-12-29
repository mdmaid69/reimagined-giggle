import os
print(os.getcwd())
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
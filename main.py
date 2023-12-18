import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
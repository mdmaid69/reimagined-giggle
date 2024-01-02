import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import os
def remove_directory(path):
        os.rmdir(path)
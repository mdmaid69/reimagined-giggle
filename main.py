import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
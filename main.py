import os
def list_files_in_directory(path):
        return os.listdir(path)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
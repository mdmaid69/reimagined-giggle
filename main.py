import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import os
def change_working_directory(path):
        os.chdir(path)
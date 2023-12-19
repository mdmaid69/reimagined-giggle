import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import sys
def add_to_python_path(path):
        sys.path.append(path)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import sys
def print_python_version():
        return sys.version
import sys
def exit_program():
        sys.exit()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
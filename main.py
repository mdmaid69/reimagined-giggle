import platform
def get_python_version():
        return platform.python_version()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
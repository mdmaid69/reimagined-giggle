import platform
def get_os_info():
        return platform.uname()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
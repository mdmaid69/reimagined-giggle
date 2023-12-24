import getpass
def get_username():
        return getpass.getuser()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
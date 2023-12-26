import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import getpass
def get_username():
        return getpass.getuser()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import getpass
def get_username():
        return getpass.getuser()
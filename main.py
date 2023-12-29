import getpass
def get_username():
        return getpass.getuser()
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
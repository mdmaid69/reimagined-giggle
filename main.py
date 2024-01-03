import getpass
def get_username():
        return getpass.getuser()
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
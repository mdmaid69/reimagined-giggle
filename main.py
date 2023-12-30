import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
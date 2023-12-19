import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
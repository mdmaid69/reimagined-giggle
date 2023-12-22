import getpass
def get_username():
        return getpass.getuser()
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
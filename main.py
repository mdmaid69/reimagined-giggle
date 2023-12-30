import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import collections
def create_user_list():
        return collections.UserList()
import collections
def create_user_list():
        return collections.UserList()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import collections
def create_user_dict():
        return collections.UserDict()
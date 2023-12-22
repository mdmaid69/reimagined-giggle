import collections
def create_stack():
        return collections.deque()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
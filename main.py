import collections
def create_stack():
        return collections.deque()
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
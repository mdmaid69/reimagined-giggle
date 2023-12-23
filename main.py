import collections
def create_queue():
        return collections.deque()
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
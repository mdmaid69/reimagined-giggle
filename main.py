import collections
def create_queue():
        return collections.deque()
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
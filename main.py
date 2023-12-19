import collections
def create_queue():
        return collections.deque()
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
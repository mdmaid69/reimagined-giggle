import time
def get_current_time():
        return time.time()
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
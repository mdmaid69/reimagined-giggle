import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import time
def get_time_since_epoch():
        return time.time()
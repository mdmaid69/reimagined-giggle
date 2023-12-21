import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
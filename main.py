import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
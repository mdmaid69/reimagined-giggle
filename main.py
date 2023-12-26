import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import datetime
def get_current_datetime():
        return datetime.datetime.now()
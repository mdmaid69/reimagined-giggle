import datetime
print(datetime.datetime.now())
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
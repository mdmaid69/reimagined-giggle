import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
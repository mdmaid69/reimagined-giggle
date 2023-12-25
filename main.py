import re
def split_string(pattern, string):
        return re.split(pattern, string)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
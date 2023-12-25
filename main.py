import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
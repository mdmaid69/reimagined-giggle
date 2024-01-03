import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
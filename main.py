import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
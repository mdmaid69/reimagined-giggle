import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
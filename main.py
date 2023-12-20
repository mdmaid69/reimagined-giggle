def calculate_average(lst):
        return sum(lst) / len(lst)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
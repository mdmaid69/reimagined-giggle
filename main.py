import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def calculate_roi(gain, cost):
        return (gain - cost) / cost